import argparse, os, yaml, pathlib
from src.sensors import SensorSuite, summarize_window
from src.lore_engine import LoreEngine
from src.codex_writer import save_artifacts, speak

def load_canon():
    canon_dir = pathlib.Path("data/canon")
    parts = []
    for p in sorted(canon_dir.glob("*.txt")):
        try:
            parts.append(p.read_text(encoding="utf-8"))
        except Exception:
            pass
    return "\n\n".join(parts)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["simulate","live"], default="simulate")
    ap.add_argument("--session", default="demo")
    ap.add_argument("--config", default="config.yaml")
    args = ap.parse_args()

    cfg = yaml.safe_load(open(args.config, "r", encoding="utf-8"))
    simulate = (args.mode == "simulate") or cfg["sensing"].get("simulate", True)

    sensors = SensorSuite(simulate=simulate, sample_rate_hz=int(cfg["sensing"]["sample_rate_hz"]))

    print(f"[MurmurBox] Collecting window for {cfg['sensing']['window_seconds']}s (simulate={simulate})...")
    samples = sensors.collect_window(seconds=int(cfg["sensing"]["window_seconds"]))
    obs = summarize_window(samples)
    obs["session"] = args.session

    canon = load_canon()
    engine = LoreEngine(
        base_url=os.getenv("OPENAI_BASE_URL", cfg["model"]["base_url"]),
        api_key=os.getenv("OPENAI_API_KEY", cfg["model"]["api_key"]),
        model_id=os.getenv("MODEL_ID", cfg["model"]["model_id"]),
        canon_text=canon
    )
    tx = engine.interpret(obs)

    session_dir = os.path.join("data", "sessions", args.session)
    pretty = save_artifacts(session_dir, obs, tx)

    print("\n=== CODEX ENTRY ===\n")
    print(pretty)

    if cfg["io"].get("speak", False):
        speak(tx.get("text",""))

if __name__ == "__main__":
    main()

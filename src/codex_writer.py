import os, json, time, subprocess

def speak(text: str):
    try:
        subprocess.run(["espeak-ng", text], check=False)
    except FileNotFoundError:
        pass

def save_artifacts(session_dir: str, observation: dict, transmission: dict):
    os.makedirs(session_dir, exist_ok=True)
    ts = transmission.get("timestamp","").replace(":","-").replace(".","-") or str(int(time.time()))
    with open(os.path.join(session_dir, f"{ts}-observation.json"), "w") as f:
        json.dump(observation, f, indent=2)
    with open(os.path.join(session_dir, f"{ts}-codex.json"), "w") as f:
        json.dump(transmission, f, indent=2)
    pretty = f"# {transmission.get('title','Transmission')}\n{transmission.get('thread','Thread-??')}\n\n{transmission.get('text','')}\n"
    with open(os.path.join(session_dir, f"{ts}-codex.txt"), "w") as f:
        f.write(pretty)
    return pretty

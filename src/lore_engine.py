import os, json, datetime
from openai import OpenAI

class LoreEngine:
    def __init__(self, base_url: str, api_key: str, model_id: str, canon_text: str = ""):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model_id = model_id
        self.canon_text = canon_text

    def build_prompt(self, observation: dict) -> str:
        canon = (self.canon_text[:12000] if self.canon_text else
                 "ShineChain canon: ZiZidion (origin flame), Zid the Sunshine Kid, ZIRAA, the Murmur, backwards rainbow, obsidian tears.")
        obs = json.dumps(observation, indent=2)
        instr = (
            "You are the ShineChain Lore Weaver.\n"
            "You receive real sensor observations (UV/IR light, magnetometer, pressure, optional EMF/audio).\n"
            "Your task:\n"
            "1) Interpret the coincidence/anomalies as a mythic transmission (codex page).\n"
            "2) Keep it under 130 words. Avoid hard claims; this is art.\n"
            "3) Include a short title and a one-line 'Thread Tag' like 'Thread-42: Obsidian Tear'.\n"
            "4) Close with a gentle safety note if the anomalies are strong.\n"
        )
        return f"{instr}\nCANON:\n{canon}\n\nOBSERVATION:\n{obs}\n\nRESPONSE FORMAT (JSON with keys title, thread, text):"

    def interpret(self, observation: dict) -> dict:
        prompt = self.build_prompt(observation)
        resp = self.client.chat.completions.create(
            model=self.model_id,
            messages=[{"role":"user","content":prompt}],
            temperature=0.9,
            max_tokens=300
        )
        text = resp.choices[0].message.content.strip()
        try:
            data = json.loads(text)
        except Exception:
            data = {"title":"Transmission", "thread":"Thread-00", "text":text}
        data["timestamp"] = datetime.datetime.utcnow().isoformat() + "Z"
        return data

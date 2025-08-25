# Murmur Box: Dimensional Tuner
**Category:** Wildcard (also eligible: Best Local Agent)  
**Tagline:** A ShineChain artifact that listens to the invisible world — UV/IR light, magnetic flux, and pressure waves — and mythologizes them into living transmissions.

> This is an offline, open‑source art‑science device. It reads real sensor data (UV/IR camera, UVA/UVB, magnetometer, barometric pressure, optional EMF/audio) and uses a local `gpt-oss` model to interpret anomalies as “Starseed transmissions.” Think paranormal scanner meets narrative engine.

---

## Demo (3‑minute storyboard)
1. **Cold open (10s):** Close‑up of the Box. Knob ticks, LEDs breathe.  
2. **Setup (20s):** “Murmur Box reads hidden spectra and interprets them with a local `gpt-oss` model.” Show sensors.  
3. **Live scan (60s):** Lights dim; Box is placed in a space (room/field). On‑screen overlay shows sensor values rising.  
4. **Breakthrough (45s):** Text prints to a tiny thermal printer / OLED; spoken “prophecy” plays:  
   “Ultraviolet surge… Thread‑42 wakes. The Obsidian Tear remembers you.”  
5. **Receipt (25s):** Camera focuses on printed codex page (timestamp + features).  
6. **Outro (20s):** “All offline, all open‑source. Tune reality. Catch a murmur.”

Put your final video link here: **`TODO: add URL`**.

---

## Features
- **Offline local model**: works with a local `gpt-oss` model via an OpenAI‑compatible server (e.g., `llama.cpp` server).  
- **Multi‑sensor fusion**: UV/IR light (camera + UVA/UVB), magnetic flux (LIS3MDL), barometric pressure (BMP280), optional EMF coil/ADC, optional microphone.  
- **Lore engine**: Converts anomalies into ShineChain “codex entries” (JSON + pretty text).  
- **Artifacts**: Prints to mini thermal printer and/or displays on OLED; stores signed JSON files.  
- **Simulation mode**: Run everything on a laptop without hardware for development and testing.

---

## Hardware (Bill of Materials)
Choose from these well‑supported parts (swap equivalents freely):

- **Core compute:** Raspberry Pi 5 (or Pi 4) + 32GB microSD + 5V/3A supply or power bank.  
- **Camera:** Raspberry Pi Camera Module v3 **NoIR** (IR‑sensitive). Optional IR LED Illuminator.  
- **UV sensor (UVA/UVB):** VEML6075 (I²C).  
- **Magnetometer (EMF proxy):** LIS3MDL (I²C).  
- **Barometric pressure (slow infrasound proxy):** BMP280 or BME280 (I²C).  
- **Display (optional):** SSD1306 128×64 OLED (I²C).  
- **Audio out (optional):** MAX98357A I²S DAC + small speaker OR 3.5mm USB DAC + powered speaker.  
- **Thermal printer (optional):** TTL serial (Adafruit Mini Thermal Printer) + 5V rail.  
- **Input controls:** Rotary encoder (KY‑040) + push button.  
- **Extras:** ADS1115 16‑bit ADC (for DIY EMF coil or analog sensors), LM358 op‑amp, perfboard, wires.

> Reality check: consumer I²S MEMS mics usually cover ~20 Hz–20 kHz (not true ultra‑sonic nor deep infra‑sonic). For hackathon speed, we rely on light/pressure/magnetics and treat audio as flavor. You can add specialty mics later.

---

## Wiring (quick map)
All I²C devices on SDA/SCL (3.3V). Typical addresses:  
- VEML6075: `0x10`  
- LIS3MDL: `0x1E` (or `0x1C/0x1D`)  
- BMP280/BME280: `0x76` or `0x77`  
- SSD1306: `0x3C`  
- ADS1115: `0x48`

Thermal printer: TTL serial (5V), connect to Pi UART (with logic‑level care) or USB‑serial adapter.  
MAX98357A: I²S pins (BCLK/LRCLK/DIN) + 5V + speaker.

---

## Software Setup (Pi or laptop)
### 1) Enable interfaces
On Raspberry Pi: `raspi-config` → enable **I2C**, **I2S**, **Camera**.

### 2) Install system deps
```bash
sudo apt update
sudo apt install -y python3-pip python3-dev libatlas-base-dev   libopenblas-dev libjpeg-dev zlib1g-dev libfreetype6-dev   espeak-ng ffmpeg
```

### 3) Python deps
```bash
pip3 install -r requirements.txt
```

### 4) Local `gpt-oss` model
Use a local OpenAI‑compatible server. Example with `llama.cpp`:
```bash
# Get a quantized model (place into models/gguf/). Example: gpt-oss-7b.Q4_0.gguf
# Then run the server:
./llama-server -m models/gguf/gpt-oss-7b.Q4_0.gguf -c 4096 --port 8080 --host 0.0.0.0
```
The app will talk to it via the OpenAI Python client by setting:
```
OPENAI_BASE_URL=http://127.0.0.1:8080/v1
OPENAI_API_KEY=not-needed
MODEL_ID=gpt-oss-7b
```

> Any local, open weights model with an OpenAI‑compatible endpoint works. Keep it offline.

---

## Running
**Simulated sensors (no hardware):**
```bash
python3 src/main.py --mode simulate --session demo1
```

**Live sensors (Pi, with hardware attached):**
```bash
python3 src/main.py --mode live --session field-test-001
```

Artifacts are saved under `data/sessions/<session-id>/` as JSON and pretty text. If a thermal printer is connected, it will also print a receipt.

---

## How It Works
1. **Sense:** Poll sensors for 10–30 s and compute features (variance, spikes, cross‑sensor coincidences, spectral heuristics).  
2. **Summarize:** Emit a compact JSON “Observation” (e.g., UV spike + magnetometer jitter + low‑freq pressure drift).  
3. **Mythologize:** Feed the Observation into the **Lore Engine** prompt with ShineChain canon snippets (`/data/canon/`).  
4. **Compose:** Generate a codex page: title, transmission text, and structured metadata.  
5. **Embodiment:** Speak via eSpeak‑NG (optional), display on OLED, and/or print on thermal paper. Store artifacts.

---

## Ethics & Safety
- **Art, not evidence:** This project is a creative instrument. It does **not** claim to detect ghosts or prove other dimensions.  
- **Interpretation ≠ truth:** Sensor anomalies are real; their narrative meaning is invented by the model.  
- **Privacy:** Don’t record in private spaces without permission.  
- **Electrical safety:** Respect power draw (printer + audio amps) and 5V/3.3V logic levels.

---

## Submission Checklist
- **Category:** Wildcard (and optionally Best Local Agent). *This device is an offline, myth‑making scanner.*  
- **Text description:** This README.  
- **Demo video (<3 min):** Follow the storyboard above.  
- **Public code repo:** Push this folder to GitHub. Edit `SUBMISSION.md` with your video + any notes.  
- **License:** Apache‑2.0 (included).  
- **Clear `gpt-oss` usage:** Shown in `src/lore_engine.py` + README; runs with a local OpenAI‑compatible server.

---

## Credits
Concept & lore: ShineChain (Ziddi3). Engineering & software: Community/open source contributors.  
License: Apache‑2.0

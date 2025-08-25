# Hackathon Submission — Echobox (Murmur Box: Dimensional Tuner)

## Category
- **Wildcard** (also eligible for **Best Local Agent**)

**Why this category?**  
It’s an embodied, offline, myth-making box that fuses physical sensors with a local `gpt-oss` model. Unexpected, artistic, experimental — and not a standard app or robot.

---

## Project Description
Echobox (Murmur Box: Dimensional Tuner) is a ShineChain-inspired artifact that listens to the invisible world — UV/IR light, magnetic flux, barometric pressure, optional EMF/audio — and mythologizes them into “codex entries.”

- Reads UV/IR light, magnetometer, and barometric pressure; optional EMF coil and audio.  
- Detects anomalies/coincidences across sensors.  
- Summarizes observations into compact JSON.  
- A local `gpt-oss` model “mythologizes” each observation into a ShineChain codex page (text + metadata).  
- Can speak or print artifacts; works fully offline.  

Think **paranormal scanner meets narrative engine**.

---

## Demo Video (3 minutes)
📺 **TODO: Add final demo link here before deadline**

Storyboard (suggested cut order):  
1. **Cold open (10s):** Close-up of the Box. Knob ticks, LEDs breathe.  
2. **Setup (20s):** “Echobox reads hidden spectra and interprets them with a local gpt-oss model.” Show sensors.  
3. **Live scan (60s):** Place Box in a space (room/field). On-screen overlay shows signals rising.  
4. **Breakthrough (45s):** Codex text prints on thermal printer / OLED. Spoken prophecy plays.  
5. **Receipt (25s):** Camera zooms on printed codex page (title + thread + prophecy).  
6. **Outro (20s):** “All offline, open-source. Tune reality. Catch a murmur.”  

---

## Features
- **Offline local model:** Works with `gpt-oss` via `llama.cpp` or compatible API server.  
- **Multi-sensor fusion:** UV/IR light, magnetometer, barometer, optional EMF/audio.  
- **Lore engine:** Translates anomalies into ShineChain codex JSON + pretty text.  
- **Artifacts:** Codex entries can be spoken aloud or printed to a thermal receipt printer.  
- **Simulation mode:** No hardware required — runs in a laptop environment.  

---

## Hardware (Bill of Materials)
- Raspberry Pi 5 (or Pi 4) + 32GB microSD + 5V/3A supply  
- Pi Camera v3 NoIR (IR-sensitive)  
- VEML6075 (UV sensor)  
- LIS3MDL (magnetometer)  
- BMP280 (barometer)  
- Optional EMF coil + ADC  
- Optional microphone  
- OLED display (SSD1306) and/or mini thermal printer  

---

## Installation & Usage
```bash
git clone https://github.com/ziddi3/Echobox.git
cd Echobox
pip install -r requirements.txt
python src/main.py --mode simulate --session demo

# Hardware Build Notes — Echobox (Murmur Box: Dimensional Tuner)

## Core Compute
- Raspberry Pi 5 (or Pi 4) with 32GB microSD
- 5V / 3A power supply
- Raspbian OS Lite

## Sensors
- Pi Camera v3 NoIR (for IR/low-light input)
- VEML6075 (UV index sensor, I²C)
- LIS3MDL (magnetometer, I²C)
- BMP280 or BME280 (barometric pressure, I²C)
- Optional: EMF coil + LM358 op-amp + ADS1115 ADC
- Optional: microphone (USB or I²S) for infrasound/ultrasound

## Output
- SSD1306 OLED (128x64, I²C) for live readings
- Mini thermal printer (TTL serial) for codex receipts
- Small speaker (via MAX98357A I²S DAC or USB audio)

## Controls
- Rotary encoder (for tuning) with push button
- LED indicators (status, anomalies)

## Notes
- Provide sufficient 5V rail power if using the printer.
- Use shielded wires for EMF coil to reduce noise.
- All sensors are optional; the system will run in simulation mode if not connected.

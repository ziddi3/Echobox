import os, time, math, random
from dataclasses import dataclass

try:
    import smbus2  # noqa
except Exception:
    smbus2 = None  # type: ignore

@dataclass
class SensorReading:
    uv_index: float = 0.0
    ir_intensity: float = 0.0
    mag_uT: float = 0.0
    pressure_hpa: float = 1013.25

class SensorSuite:
    def __init__(self, simulate: bool = True, sample_rate_hz: int = 10):
        self.simulate = simulate
        self.sample_rate_hz = sample_rate_hz
        # TODO: add real I2C init here for live mode

    def read_once(self) -> SensorReading:
        if self.simulate:
            t = time.time()
            uv = max(0.0, 0.5 + 0.5*math.sin(t/7.0) + random.uniform(-0.1,0.1))
            if random.random() < 0.03: uv += random.uniform(0.8, 1.5)

            ir = max(0.0, 0.4 + 0.4*math.sin(t/5.0 + 1.0) + random.uniform(-0.1,0.1))
            if random.random() < 0.02: ir += random.uniform(0.7, 1.2)

            mag = 45.0 + 2.0*math.sin(t/11.0) + random.uniform(-0.8,0.8)
            if random.random() < 0.02: mag += random.uniform(5, 12)

            p = 1013.25 + 0.5*math.sin(t/17.0) + random.uniform(-0.2,0.2)
            return SensorReading(uv_index=uv, ir_intensity=ir, mag_uT=mag, pressure_hpa=p)
        else:
            # TODO: replace with real sensor reads
            return SensorReading()

    def collect_window(self, seconds: int = 20):
        n = max(1, int(seconds * self.sample_rate_hz))
        data = []
        for _ in range(n):
            data.append(self.read_once().__dict__)
            time.sleep(1.0/self.sample_rate_hz)
        return data

def summarize_window(samples):
    if not samples:
        return {"error":"no_samples"}
    import numpy as np
    uv = np.array([s["uv_index"] for s in samples])
    ir = np.array([s["ir_intensity"] for s in samples])
    mg = np.array([s["mag_uT"] for s in samples])
    pr = np.array([s["pressure_hpa"] for s in samples])

    def feats(x):
        return dict(mean=float(x.mean()), std=float(x.std()), max=float(x.max()), min=float(x.min()))

    uvf, irf, mgf, prf = feats(uv), feats(ir), feats(mg), feats(pr)

    uv_spike = float((uv[-1] - uv.mean())/ (uv.std()+1e-6))
    ir_spike = float((ir[-1] - ir.mean())/ (ir.std()+1e-6))
    mg_jitter = float(mg.std())
    pr_drift = float(pr[-1] - pr[0])

    return {
        "window_seconds": len(samples),
        "features": {
            "uv": {**uvf, "z_last": uv_spike},
            "ir": {**irf, "z_last": ir_spike},
            "mag": mgf,
            "pressure": {**prf, "drift": pr_drift},
            "coincidence_score": float((max(0,uv_spike)+max(0,ir_spike)) * (1.0 + mg_jitter/5.0))
        }
    }

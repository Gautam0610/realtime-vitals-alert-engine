
import time
import random
import json

def generate_vitals():
    # Simulate realistic vital signs
    heart_rate = random.randint(60, 100)
    blood_pressure_systolic = random.randint(110, 140)
    blood_pressure_diastolic = random.randint(70, 90)
    oxygen_saturation = random.randint(95, 100)
    temperature = round(random.uniform(36.5, 37.5), 1)

    vitals = {
        "heart_rate": heart_rate,
        "blood_pressure_systolic": blood_pressure_systolic,
        "blood_pressure_diastolic": blood_pressure_diastolic,
        "oxygen_saturation": oxygen_saturation,
        "temperature": temperature,
        "timestamp": time.time()
    }
    return vitals


def generate_anomaly(vitals):
    # Introduce anomalies with a certain probability
    if random.random() < 0.1:  # 10% chance of anomaly
        vitals["heart_rate"] = random.randint(120, 160)  # High heart rate
    return vitals

if __name__ == '__main__':
    while True:
        vitals = generate_vitals()
        vitals = generate_anomaly(vitals)
        print(json.dumps(vitals))
        time.sleep(1)

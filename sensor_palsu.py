import paho.mqtt.client as mqtt
import random
import time
import json

MQTT_BROKER = "mqtt.tyoprakusudewo.bond"
MQTT_PORT = 1883
MQTT_TOPIC = "sensor/suhu"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

print(f"Sensor palsu jalan, kirim ke {MQTT_BROKER}")

try:
    while True:
        suhu = round(random.uniform(25, 35), 1)
        kelembaban = round(random.uniform(50, 85), 1)
        data = {"suhu": suhu, "kelembaban": kelembaban}
        client.publish(MQTT_TOPIC, json.dumps(data))
        print(f"Kirim: suhu={suhu}°C, kelembaban={kelembaban}%")
        time.sleep(5)
except KeyboardInterrupt:
    print("Berhenti.")
    client.disconnect()

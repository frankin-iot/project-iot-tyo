import paho.mqtt.client as mqtt
import random
import time
import json

# ========== KONFIGURASI ==========
MQTT_BROKER = "100.103.36.119"   # IP UBUNTU LO!
MQTT_PORT = 1883               # 🔥 PORT MQTT BROKER (BUKAN WEBSOCKET!)
MQTT_TOPIC = "sensor/suhu"     # WAJIB SAMA DENGAN DASHBOARD!

# ========== KONEK KE MQTT ==========
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(MQTT_BROKER, MQTT_PORT, 60)

print("=" * 50)
print(" SENSOR PALSU - TYO HEBAT ")
print("=" * 50)
print(f"✅ Broker: {MQTT_BROKER}:{MQTT_PORT}")
print(f"📡 Topic: {MQTT_TOPIC}")
print("📤 Kirim data tiap 2 detik...")
print("Tekan Ctrl+C untuk berhenti\n")

try:
    while True:
        suhu = round(random.uniform(26.0, 32.0), 1)
        kelembaban = round(random.uniform(55.0, 75.0), 1)
        
        data = {
            "suhu": suhu,
            "kelembaban": kelembaban
        }
        
        client.publish(MQTT_TOPIC, json.dumps(data))
        print(f"📤 Kirim: suhu={suhu}°C, kelembaban={kelembaban}%")
        time.sleep(2)

except KeyboardInterrupt:
    print("\n⏹️ Sensor dimatiin.")
finally:
    client.disconnect()
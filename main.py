import time
import network
from machine import Pin, ADC
import blynklib

# --- Konfigurasi WiFi & Blynk ---
WIFI_SSID = 'kuciangkantuik'
WIFI_PASS = 'abcd1234'
BLYNK_AUTH = 'vD8YEPH1X7MSBz2SuBBTX9MvXae9S2Om'

# --- Inisialisasi Pin ---
sensor_pin = ADC(Pin(32))  # Sensor kelembapan tanah
sensor_pin.atten(ADC.ATTN_11DB)  # Rentang pembacaan 0-3.6V
sensor_pin.width(ADC.WIDTH_12BIT)

relay_pin = Pin(4, Pin.OUT)
relay_pin.value(1)  # Matikan pompa saat awal (HIGH = OFF)

# --- Variabel kontrol manual ---
manual_mode = False
manual_state = False

# --- Koneksi WiFi ---
print("Menghubungkan ke WiFi...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)

while not wifi.isconnected():
    print(".", end="")
    time.sleep(0.5)
print("\nWiFi connected:", wifi.ifconfig())

# --- Inisialisasi Blynk ---
blynk = blynklib.Blynk(BLYNK_AUTH)

# --- Fungsi ketika tombol di Blynk ditekan (V1) ---
@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    global manual_mode, manual_state
    if int(value[0]) == 1:
        manual_mode = True
        manual_state = True
        print("🟡 Manual Mode ON → Pompa Menyala")
    else:
        manual_mode = False
        manual_state = False
        print("🟢 Kembali ke Mode Otomatis")

# --- Fungsi utama pengecekan kelembapan ---
def check_soil():
    raw = sensor_pin.read()
    moisture = int((4095 - raw) / 4095 * 100)  # Persentase (semakin kering = lebih tinggi)

    print(f"Raw ADC: {raw} | Moisture: {moisture} %")
    blynk.virtual_write(0, moisture)

    if not manual_mode:
        if moisture < 30:
            relay_pin.value(0)  # ON
            print("💧 Mode Otomatis: Tanah kering → Pompa ON")
        else:
            relay_pin.value(1)  # OFF
            print("💧 Mode Otomatis: Tanah cukup → Pompa OFF")
    else:
        if manual_state:
            relay_pin.value(0)
            print("🔧 Mode Manual: Pompa ON")
        else:
            relay_pin.value(1)
            print("🔧 Mode Manual: Pompa OFF")

# --- Loop utama ---
while True:
    blynk.run()
    check_soil()
    time.sleep(2)

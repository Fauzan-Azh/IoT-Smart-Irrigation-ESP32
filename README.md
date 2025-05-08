# 🌿 IoT Smart Irrigation System with ESP32

## 👥 Anggota Kelompok 8
- Fauzan Azhima (105222003)
- Ridho Pratama (105222011)

## 📄 Deskripsi Singkat
Proyek ini merupakan sistem irigasi otomatis berbasis IoT yang menggunakan ESP32 dan sensor kelembaban tanah. Sistem ini mampu menyiram tanaman secara otomatis ketika tanah terdeteksi kering dan dapat dikendalikan dari jarak jauh melalui aplikasi Blynk. Proyek ini dibuat sebagai tugas besar mata kuliah *Mikrokontroler dan IoT* oleh Kelompok 8.

## 🎯 Tujuan
- Mengembangkan sistem irigasi berbasis mikrokontroler yang terhubung ke internet.
- Mengotomatisasi proses penyiraman tanaman berdasarkan kondisi lingkungan.
- Memberikan solusi sederhana untuk efisiensi penggunaan air dan tenaga dalam pertanian kecil.
- Melatih kemampuan integrasi sensor, mikrokontroler, dan platform IoT.

## 🌍 SDGs yang Disasar
**SDG 2: Zero Hunger**  
Proyek ini mendukung upaya peningkatan produktivitas pertanian dan efisiensi air dengan menyediakan sistem penyiraman tanaman otomatis berbasis data kelembaban tanah.

## 🔁 Skema Blok Sistem
### 📥 Input → ⚙️ Proses → 📤 Output

ESP32 membaca kelembaban tanah, menampilkan data ke LCD, dan menyiram tanaman otomatis saat tanah kering. Data dan kontrol juga bisa dilakukan lewat aplikasi Blynk.

## 🔩 Daftar Komponen yang Digunakan
| No | Komponen                 | Jumlah | Keterangan                                 |
|----|--------------------------|--------|--------------------------------------------|
| 1  | ESP32 Board              | 1      | Mikrokontroler utama dengan WiFi           |
| 2  | Soil Moisture Sensor     | 1      | Sensor kelembaban tanah                    |
| 3  | Breadboard               | 1      | Perakitan rangkaian sementara              |
| 4  | ESP32 Board Adapter      | 1      | Untuk memasang ESP32 agar lebih kompleks   |
| 5  | Relay Module             | 1      | Mengendalikan arus ke pompa air            |
| 6  | LCD 16x2 + I2C Module    | 1      | Menampilkan data kelembaban tanah          |
| 7  | Jumper Wires             | Beberapa | Koneksi antar komponen                   |
| 8  | Mini Water Pump (DC)     | 1      | Menyiram tanaman secara otomatis           |
| 9  | Mini Water Pipe          | 1      | Saluran air dari pompa ke tanaman          |
| 10 | Li-ion Battery + Holder  | 1 set  | Sumber daya portable untuk ESP32 & pompa   |


---

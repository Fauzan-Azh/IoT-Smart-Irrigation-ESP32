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
| 4  | Relay Module             | 1      | Mengendalikan arus ke pompa air            |
| 5  | Jumper Wires             | Beberapa | Koneksi antar komponen                   |
| 6  | Mini Water Pump (DC)     | 1      | Menyiram tanaman secara otomatis           |
| 7  | Mini Water Pipe          | 1      | Saluran air dari pompa ke tanaman          |
| 8  | Li-ion Battery + Holder  | 1 set  | Sumber daya portable untuk pompa           |


## 🔁 Diagram Blok Sistem

![Diagram Blok Sistem](./Tubes%20IOT-Diagram%20blok%20sistem.jpg)

Diagram blok ini menggambarkan alur logika dari sistem irigasi otomatis berbasis IoT. Sistem diawali dengan inisialisasi sensor dan perangkat kontrol seperti ESP32, relay, dan koneksi ke platform Blynk. Selanjutnya, sensor kelembapan tanah membaca kadar air di dalam tanah secara berkala.

Jika kondisi tanah terdeteksi kering (di bawah 30%), ESP32 akan mengaktifkan relay untuk menyalakan pompa air. Data pembacaan kelembapan dan status pompa kemudian dikirimkan secara real-time ke aplikasi Blynk. Proses pembacaan dan pengambilan keputusan ini diulang terus menerus selama sistem aktif, memberikan otomatisasi dan kontrol jarak jauh bagi pengguna.

## ⚙️ Implementasi Hardware

![Implementasi Hardware](./implementasi%20hardware.jpg)

Berikut adalah komponen utama dan koneksi dalam sistem:

### 🔌 Komponen:
- **ESP32** – pusat kontrol sistem, membaca data dari sensor, mengaktifkan relay, dan mengirim data ke Blynk.
- **Soil Moisture Sensor** – mendeteksi tingkat kelembapan tanah dan memberikan data analog ke ESP32 (GPIO 32).
- **Relay Module** – mengontrol aliran daya ke pompa air (GPIO 4).
- **Mini Water Pump** – menyiram tanaman saat relay diaktifkan.
- **Power Supply 5VDC** – digunakan sebagai sumber daya eksternal untuk pompa air.

### 🔗 Skema Koneksi:
- Sensor dan relay mendapat daya dari pin 3V3 dan GND ESP32.
- Output analog sensor ke GPIO 32.
- Sinyal kontrol relay ke GPIO 4.
- Pompa air dihubungkan ke terminal NO dan COM relay.
- Ground dari seluruh perangkat disatukan sebagai common ground untuk kestabilan sistem.

## 📱 Integrasi Blynk

Sistem terintegrasi dengan platform **Blynk IoT** yang memungkinkan pengguna:
- Melihat kelembapan tanah (via **Virtual Pin V0**),
- Mengontrol pompa air secara manual (via **Virtual Pin V1**),
- Mengakses dari **aplikasi mobile** dan **web dashboard** secara real-time,
- Mendapatkan kontrol dan monitoring jarak jauh tanpa harus menggunakan server lokal.

## 📱 Tampilan Aplikasi Blynk

### Aplikasi Mobile

![Tampilan Blynk Mobile](./iPhone%2016%20-%201.png)

- Menampilkan **gauge** nilai kelembapan tanah (V0).
- Tombol **ON/OFF** kontrol manual pompa (V1).

### Blynk Web Dashboard

![Tampilan Web Dashboard](./tampilan%20web.png)

- Memantau status kelembapan dan pompa secara real-time.
- Tersedia histori data dan pengelolaan perangkat.
- Akses via: [https://blynk.cloud](https://blynk.cloud)

---

## 📌 Fitur Utama
- Otomatis menyiram tanaman saat tanah kering.
- Kontrol pompa secara manual dari jarak jauh.
- Real-time monitoring dari smartphone atau laptop.
- Hemat air dan cocok untuk pertanian skala kecil.
- Bisa dikembangkan dengan sensor tambahan dan logging data.

---

---

## 📜 Lisensi
MIT License – bebas digunakan untuk pembelajaran, pengembangan lebih lanjut, dan proyek sosial.


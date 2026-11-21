# 🔥 PANDUAN RESMI & CARA PEMASANGAN — NATHAN FELIX LIVE BRIDGE v3.0 🔥
**Enterprise DevOps & Real-Time SFTP Pipeline — Dirancang oleh Nathan Felix**

Halo! Selamat datang di tool sinkronisasi otomatis **Nathan Felix Live Bridge**. Tool ini memungkinkan kamu untuk melakukan *live coding* di laptop Windows (menggunakan VS Code / Antigravity / Cursor) dan kode kamu akan otomatis ter-upload ke server Linux Ubuntu secara real-time (< 50ms) setiap kali kamu mengeklik Save TANPA perlu ribet!

Karena tool ini dijalankan langsung via Python murni (`.py`) dan bukan file `.exe`, **antivirus Windows Defender atau Microsoft SmartScreen tidak akan pernah memblokir aplikasi ini!**

---

## 🚀 1. CARA PEMASANGAN DI PROYEK KAMU (SANGAT MUDAH & OTOMATIS!)

Ketika kamu menerima folder **`felix_bridge/`** ini dari Nathan Felix, kamu hanya perlu melakukan 2 langkah mudah berikut:

### 📍 Langkah 1: Masukkan Folder ke Dalam Proyek
Salin atau letakkan seluruh folder **`felix_bridge/`** ke dalam folder proyek web / Laravel kamu (proyek apa saja, tidak peduli apa nama foldernya!).

### 📍 Langkah 2: KLIK GANDA FILE PEMASANG OTOMATIS! *(NEW FEATURE!)*
Buka folder `felix_bridge/`, lalu **klik ganda (double-click)** pada file:
👉 **`KLIK_UNTUK_PASANG.cmd`** *(atau `INSTALL_BRIDGE.cmd`)*

**Apa yang terjadi?**
Dalam 1 detik, skrip otomatis ini akan menyalin ke-4 file launcher (`gui.py`, `gui.cmd`, `connect.py`, `connect.cmd`) **KE LUAR FOLDER** secara otomatis langsung ke root proyek kamu! Kamu **tidak perlu lagi melakukan copy-paste manual** atau mengetahui nama folder proyekmu!

```text
📁 FOLDER PROYEK KAMU/ (Root - Nama bebas apa saja!)
│
├── 🚀 gui.py & gui.cmd              <--- [DIPASANG OTOMATIS!] Untuk membuka UI Grafis
├── 🚀 connect.py & connect.cmd      <--- [DIPASANG OTOMATIS!] Untuk membuka UI Terminal
│
├── 📁 felix_bridge/                 <--- [TETAP DI DALAM] Folder mesin & library inti
│   ├── ⚡ KLIK_UNTUK_PASANG.cmd     <--- [KLIK INI!] Pemasang otomatis ke luar folder
│   ├── felix_app.py                 <--- Mesin GUI (Jangan dipindahkan)
│   ├── felix_terminal.py            <--- Mesin Terminal (Jangan dipindahkan)
│   └── PANDUAN_SETUP_TEMAN.md       <--- Buku panduan ini
│
├── 📁 app/                          <--- Folder kode web kamu
├── 📁 resources/                    <--- Folder tampilan web kamu
└── ...
```

---

## ❓ 2. MENGAPA LAUNCHER HARUS DIPASANG DI LUAR?

* **Mengapa `gui.py` dan `connect.py` HARUS berada di LUAR (di root proyek)?**
  Karena file launcher ini bertugas sebagai **"Mata dan Jembatan"**! Saat kamu menjalankan `gui.cmd` dari luar (root folder), aplikasi akan mendeteksi dan memantau seluruh folder proyek kamu (`app/`, `resources/`, dll). Setiap ada file yang berubah atau disimpan, file tersebut langsung dikirim ke server Linux dalam waktu 0.04 detik!
  *(Jika launcher ini tetap di dalam folder `felix_bridge/`, dia hanya akan memantau folder bridge itu sendiri dan tidak bisa menemukan kode web kamu!)*

* **Mengapa file mesin tetap di dalam?**
  `felix_app.py` dan `felix_terminal.py` adalah *"Ruang Mesin"*. Dengan membiarkannya tetap di dalam folder `felix_bridge/`, proyek utama kamu tetap terlihat sangat rapi, bersih, dan profesional!

---

## 💻 3. CARA MENGGUNAKAN (LIVE CODING)

Setelah kamu mengeklik `KLIK_UNTUK_PASANG.cmd`, kembali ke folder utama (root) proyek kamu:

1. **Pastikan Python Sudah Terinstall:**
   Pastikan laptop kamu sudah menginstall Python (dan centang *"Add Python to PATH"* saat instalasi).
2. **Jalankan Aplikasi dari Folder Utama:**
   - **Versi GUI (Tampilan Mewah Grafis):** Klik ganda pada file **`gui.cmd`** yang sudah ada di luar.
   - **Versi Terminal (Sangat Ringan):** Klik ganda pada file **`connect.cmd`** yang sudah ada di luar.
3. **Instalasi Library Otomatis:**
   Saat pertama kali dijalankan, skrip `.cmd` akan otomatis memeriksa dan menginstall library yang dibutuhkan (`customtkinter`, `pillow`, `paramiko`) secara otomatis!
4. **Masukkan Lisensi & IP Server:**
   Ikuti petunjuk di layar untuk memasukkan Kode Lisensi VIP dari Nathan Felix, IP Server Linux, Username, Password, dan jalur folder Linux (contoh: `/var/www/corporat`).
5. **Mulai Live Coding!**
   Buka file apa saja di VS Code atau Antigravity, lakukan perubahan, dan tekan **Ctrl + S**. Lihat layar konsol—kode kamu langsung ter-upload dan tersinkron secara live ke Linux!

---

## 💡 BUTUH BANTUAN?
Hubungi **Nathan Felix** selaku Pencipta & Arsitek Utama sistem Live Bridge Pipeline ini!

Siap 👍
Aku buatkan **README.md yang rapi, detail, dan profesional**, sesuai **struktur folder kamu sekarang** dan cocok untuk **developer lain yang mau clone & jalanin OCR PaddleOCR ini**.

Kamu bisa **langsung copy–paste** ke `README.md`.

---

```md
# OCR Service – PaddleOCR (Python)

Service OCR berbasis **PaddleOCR (Python)** yang digunakan untuk mengekstrak teks dari file gambar / dokumen.
Project ini dirancang sebagai **service terpisah** yang bisa diintegrasikan dengan backend lain (contoh: Laravel).

---

## 📂 Struktur Folder

```

OCR-SERVICE/
├── app/
│   ├── services/
│   │   └── paddleocr/
│   │       ├── **init**.py
│   │       ├── ocr.py          # Logic utama OCR PaddleOCR
│   │       └── main.py         # Entry point / runner
│   └── **pycache**/
│
├── uploads/                   # Folder runtime upload (tidak di-push ke GitHub)
├── venv/                      # Virtual environment (tidak di-push)
├── .gitignore
└── README.md

````

---

## ⚙️ Prasyarat

Pastikan environment kamu sudah memenuhi syarat berikut:

- **Python 3.9+** (disarankan 3.10)
- **Git**
- OS: Windows / Linux / macOS

Cek versi Python:
```bash
python --version
````

---

## 📥 Clone Repository

Clone project dari GitHub:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd OCR-SERVICE
```

> Ganti `USERNAME/REPOSITORY` sesuai repo kamu.

---

## 🐍 Membuat Virtual Environment

Disarankan **SELALU menggunakan virtual environment** agar dependency terisolasi.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Jika berhasil, terminal akan berubah menjadi:

```
(venv)
```

---

## 📦 Install Dependency

Install semua dependency dari `requirements.txt`:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Jika belum ada `requirements.txt`, buat dengan:

```bash
pip freeze > requirements.txt
```

---

## 📁 Folder `uploads`

Folder `uploads/` digunakan untuk **menyimpan file sementara** (gambar / dokumen) yang akan diproses OCR.

> Folder ini **tidak ikut GitHub** (sudah di-ignore di `.gitignore`).

Jika belum ada, buat manual:

```bash
mkdir uploads
```

---

## ▶️ Menjalankan OCR Service

Masuk ke folder paddleocr:

```bash
cd app/services/paddleocr
```

Jalankan service:

```bash
python main.py
```

Jika berhasil, service siap menerima proses OCR.

---

## 🧠 Cara Kerja Singkat

1. File gambar/dokumen disimpan sementara di folder `uploads/`
2. `ocr.py` memproses file menggunakan **PaddleOCR**
3. Hasil OCR berupa **raw text**
4. Output bisa dikirim kembali ke backend (Laravel / API / CLI)

---

## 🔗 Integrasi dengan Backend (Laravel)

Biasanya service ini:

* Dipanggil via **command / API**
* Backend hanya mengirim **path file**
* OCR service mengembalikan **hasil text**

Contoh alur:

```
Laravel Upload → Python OCR → Raw Text → Simpan ke Database
```

---

## 🚫 File yang Tidak Masuk GitHub

Berikut file/folder yang **dikecualikan**:

* `venv/`
* `uploads/`
* `__pycache__/`
* `.env`

Semua aturan ada di `.gitignore`.

---

## 📌 Catatan Penting

* Jangan upload `venv/` ke GitHub
* Jangan commit file hasil OCR
* Gunakan environment terpisah untuk production
* Pastikan PaddleOCR sesuai arsitektur OS (CPU/GPU)

---

## 👨‍💻 Author

Dikembangkan oleh **Rizky Ramadhan**
OCR Service menggunakan **PaddleOCR (Python)**

---

## 📄 License

Project ini bebas digunakan untuk kebutuhan internal / pembelajaran.

```

---

Kalau mau, aku bisa:
- 🔥 Sesuaikan README untuk **production**
- 🔥 Tambahin **API usage example**
- 🔥 Buatin **Docker + docker-compose**
- 🔥 Buatin **diagram arsitektur Laravel ↔ Python OCR**

Tinggal bilang mau lanjut ke mana 🚀
```

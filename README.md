
---

# OCR Service — PaddleOCR (Python)

Layanan OCR (Optical Character Recognition) berbasis **PaddleOCR** untuk ekstraksi teks dari gambar atau dokumen. Arsitektur ini dirancang sebagai *microservice* mandiri yang menjadi pelengkap untuk repositori **[Bill Check](https://github.com/KateKateline/bill-check)**.

## 🚀 Fitur Utama

* **High Accuracy:** Menggunakan engine PaddleOCR yang dioptimalkan.
* **Multi-format Support:** Mendukung ekstraksi teks dari berbagai format gambar dan dokumen.
* **Decoupled Architecture:** Berjalan sebagai service terpisah untuk menjaga backend tetap ringan.

---

## 🛠 Prasyarat Sistem

* **OS:** Windows.
* **Git:** Untuk manajemen repositori.
* **Python:** v3.10.x

### Instalasi Python 3.10 (Windows)

Jika Anda belum memiliki Python 3.10, jalankan perintah ini di PowerShell untuk mengunduh dan menginstal secara otomatis:

```powershell
winget install Python.Python.3.10

```

---

## 💻 Panduan Instalasi

### 1. Kloning Repositori

```bash
git clone https://github.com/KateKateline/paddle-ocr-service.git
cd paddle-ocr-service

```

### 2. Konfigurasi Virtual Environment (VENV)

```bash
py -3.10 -m venv venv

```

### 3. Instalasi Dependency

Pastikan virtual environment sudah aktif (muncul tanda `(venv)`), lalu jalankan:

```bash
pip install --upgrade pip
pip install python-multipart
pip install paddlepaddle paddleocr fastapi uvicorn

```

---

## ⚙️ Menjalankan Service

Jalankan service utama langsung dari root project menggunakan Uvicorn:

```bash
uvicorn app.main:app --reload

```

---

## 📝 Note

Service ini berfungsi untuk menerima kiriman gambar dari **[Bill Check](https://github.com/KateKateline/bill-check)** dan mengembalikan hasil pembacaan teks (raw text) untuk diproses lebih lanjut oleh sistem utama.

---

# OCR Service — PaddleOCR (Python)

Layanan OCR sederhana berbasis PaddleOCR (Python) untuk mengekstrak teks dari gambar atau dokumen. Dirancang sebagai service terpisah yang mudah diintegrasikan dengan backend lain (mis. Laravel).

## Fitur
- Ekstraksi teks dari gambar/dokumen
- Output berupa teks mentah (raw text)
- Dijalankan sebagai service terpisah — cocok diintegrasikan lewat command atau API

## Prasyarat
- Python 3.9+ (disarankan 3.10)
- Git
- OS: Windows / Linux / macOS

Periksa versi Python:

```bash
python --version
```
````

---

## Instalasi

Clone repository:

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd OCR-SERVICE
```

> Ganti `USERNAME/REPOSITORY` sesuai repo kamu.

---

## Virtual environment (disarankan)

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Setelah aktif, prompt akan menampilkan `(venv)`.

---

## Install dependency

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Jika belum ada `requirements.txt`, buat dengan `pip freeze > requirements.txt` setelah menginstall dependency yang diperlukan.

---

## Folder `uploads`

Gunakan folder `uploads/` untuk menyimpan file sementara yang akan diproses OCR. Folder ini di-ignore dari Git (lihat `.gitignore`).

Jika belum ada, buat dengan:

```bash
mkdir uploads
```

---

## Menjalankan service

Jalankan dari root project (direkomendasikan):

```bash
python app/main.py
```

Atau jika ada entrypoint di folder service:

```bash
cd app/services/paddleocr
python main.py
```

Jika berjalan, service akan siap menerima permintaan OCR.

---

## Cara kerja singkat

1. File disimpan sementara di `uploads/`
2. `ocr.py` memproses file menggunakan PaddleOCR
3. Hasil berupa teks mentah (raw text)
4. Backend menerima path file dan mengolah hasil teks sesuai kebutuhan

---

## Integrasi dengan backend

Umumnya dipakai lewat command atau API. Backend mengirimkan path file, service mengembalikan hasil teks.

Contoh alur:

Laravel Upload → Python OCR → Raw Text → Simpan ke Database

---

## File yang dikecualikan dari Git

- `venv/`
- `uploads/`
- `__pycache__/`
- `.env`

Aturan lengkap ada di `.gitignore`.

---

## Catatan penting

- Jangan mengunggah `venv/` ke GitHub
- Jangan commit file hasil OCR
- Gunakan environment terpisah untuk production
- Pastikan build PaddleOCR sesuai arsitektur (CPU/GPU)

---

## Author

Dikembangkan oleh Rizky Ramadhan

## Lisensi

Bebas digunakan untuk keperluan internal dan pembelajaran.

---

Jika ingin, saya bisa bantu:
- Menyusun README khusus produksi
- Menambahkan contoh penggunaan API/CLI
- Menambahkan Docker + docker-compose
- Membuat diagram arsitektur integrasi

Beritahu bagian mana yang ingin Anda kembangkan selanjutnya.

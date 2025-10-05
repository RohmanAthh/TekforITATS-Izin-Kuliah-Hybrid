# 🎓 TekforITATS - Izin Kuliah Hybrid

Program Izin Kuliah Hybrid Dibuat Oleh Abdurrahman Athaillah TekforITATS 2024

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3+-purple.svg)](https://getbootstrap.com/)

> **Aplikasi Web Modern untuk Pembuatan Surat Izin Kuliah Online** ✨

Proyek ini adalah aplikasi web yang dirancang khusus untuk mahasiswa Teknik Informatika ITATS untuk memudahkan pembuatan surat izin kuliah secara online. Dengan antarmuka yang elegan dan fitur-fitur canggih, aplikasi ini mendukung pembelajaran hybrid untuk kelas pagi dan malam.

## 🌟 Fitur Utama

### 📝 **Formulir Interaktif**
- **Multi-Select Minggu**: Pilih beberapa minggu pertemuan dengan mudah menggunakan tombol interaktif
- **Validasi Real-time**: Input validation untuk memastikan data yang lengkap dan akurat
- **Tanda Tangan Digital**: Fitur signature pad untuk tanda tangan elektronik

### 🎨 **Desain Modern**
- **UI/UX Elegan**: Gradient background dengan efek glassmorphism
- **Responsive Design**: Kompatibel dengan desktop dan mobile
- **Animasi Smooth**: Transisi dan efek hover yang menarik
- **Dark Mode Ready**: Tema yang dapat dikustomisasi

### 📚 **Dukungan Mata Kuliah**
- **Kelas Malam**: Dropdown mata kuliah dan dosen pengampu yang sudah terintegrasi
- **Kelas Pagi**: Input manual untuk mata kuliah dan dosen baru
- **Auto-Mapping**: Otomatis mengisi dosen berdasarkan mata kuliah yang dipilih

### 📄 **Generate Surat**
- **Template Word**: Menggunakan template DOCX yang profesional
- **Konversi PDF**: Otomatis convert ke PDF menggunakan LibreOffice
- **Format Tanggal**: Format tanggal Indonesia yang benar

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- LibreOffice (untuk konversi PDF)
- Git

### Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/RohmanAthh/TekforITATS-Izin-Kuliah-Hybrid.git
   cd TekforITATS-Izin-Kuliah-Hybrid
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Application**
   ```bash
   python program.py
   ```

4. **Open Browser**
   ```
   http://localhost:5000
   ```

## 📖 Cara Penggunaan

1. **Isi Data Mahasiswa**: Masukkan NPM, nama, program studi, dan kelas
2. **Pilih Kelas**: Sistem akan menyesuaikan form berdasarkan kelas (malam/pagi)
3. **Pilih Mata Kuliah & Dosen**: Untuk kelas malam, pilih dari dropdown; untuk pagi, input manual
4. **Pilih Minggu**: Klik tombol minggu yang ingin diizinkan (multiple selection)
5. **Isi Alasan & Tanggal**: Berikan alasan izin dan tanggal surat
6. **Tanda Tangan**: Gunakan signature pad untuk tanda tangan digital
7. **Generate Surat**: Klik "Buat Surat" untuk mendapatkan file PDF

## 🛠️ Teknologi

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Template Engine**: Jinja2
- **Document Processing**: python-docx, docxtpl
- **PDF Conversion**: LibreOffice (soffice)
- **Icons**: Bootstrap Icons

## 📁 Struktur Proyek

```
TekforITATS-Izin-Kuliah-Hybrid/
├── program.py              # Main Flask application
├── requirements.txt        # Python dependencies
├── template_surat.docx     # Word template
├── tanda_tangan.png        # Signature placeholder
├── templates/
│   └── form.html          # Main form template
├── Dockerfile             # Docker configuration
├── Procfile              # Heroku deployment
└── README.md             # This file
```

## 🎯 Fitur Khusus

### Multi-Select Minggu
```html
<!-- Tombol interaktif untuk memilih minggu -->
<label class="btn btn-outline-primary">
  <input type="checkbox" name="pertemuan[]" value="Minggu ke1">
  Minggu Ke-1
</label>
```

### Responsive Grid
```html
<!-- Grid 4x4 untuk pemilihan minggu -->
<div class="row g-2">
  <div class="col-3">
    <!-- Tombol minggu -->
  </div>
</div>
```

### Dynamic Form
```javascript
// JavaScript untuk menyesuaikan form berdasarkan kelas
function updateMatkulDosenByKelas() {
  // Logic untuk show/hide fields
}
```

## 🌐 Deployment

### Heroku
1. Install Heroku CLI
2. Login ke Heroku
   ```bash
   heroku login
   ```
3. Create app
   ```bash
   heroku create your-app-name
   ```
4. Deploy
   ```bash
   git push heroku main
   ```

### Docker
```bash
docker build -t izin-kuliah .
docker run -p 5000:5000 izin-kuliah
```

## 🤝 Kontribusi

Kami sangat terbuka untuk kontribusi! Silakan:

1. Fork repository
2. Buat branch fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 Lisensi

Distributed under the MIT License. See `LICENSE` for more information.

## 👨‍💻 Developer

**TekforITATS2024** - *Initial work* - [RohmanAthh](https://github.com/RohmanAthh)

## 🙏 Acknowledgments

- Teknik Informatika ITATS
- Bootstrap Team
- Flask Community
- Semua kontributor open source

---

<div align="center">

**Made with ❤️ by TekforITATS2024**

© 2025 Teknik Informatika ITATS. All rights reserved.

[⭐ Star this repo](https://github.com/RohmanAthh/TekforITATS-Izin-Kuliah-Hybrid) | [🐛 Report Bug](https://github.com/RohmanAthh/TekforITATS-Izin-Kuliah-Hybrid/issues) | [✨ Request Feature](https://github.com/RohmanAthh/TekforITATS-Izin-Kuliah-Hybrid/issues)

</div>

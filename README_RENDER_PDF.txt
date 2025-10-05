Agar konversi DOCX ke PDF otomatis berjalan di Render, pastikan image Docker/Runtime Render Anda mendukung LibreOffice (soffice).

Jika menggunakan Render native Python, tambahkan build command berikut di pengaturan Render agar LibreOffice terinstall:

apt-get update && apt-get install -y libreoffice

Atau gunakan Dockerfile custom dengan baris:
RUN apt-get update && apt-get install -y libreoffice

Tanpa LibreOffice, fitur konversi PDF tidak akan berjalan di Render.

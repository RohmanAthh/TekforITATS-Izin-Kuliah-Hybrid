from flask import Flask, render_template, request, send_file, redirect, url_for
import subprocess
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches
import base64, time, os
from datetime import datetime

app = Flask(__name__)
last_pdf = None

@app.route("/", methods=["GET"])
def index():
    return render_template("form.html")

@app.route("/generate", methods=["POST"])
def generate():
    global last_pdf
    nama = request.form["nama"]
    npm = request.form["npm"]
    program = request.form["program"]
    instansi = request.form["instansi"]
    matakul = request.form["matakul"]
    dosen = request.form["dosen"]
    kelas = request.form["kelas"]
    pertemuan = request.form["pertemuan"]
    tanggal = request.form["tanggal"]
    alasan = request.form["alasan"]
    tanggal_surat = request.form["tanggal_surat"]
    ttd_base64 = request.form["tanda_tangan"]

    # load template docx
    doc = DocxTemplate("template_surat.docx")

    tanda_tangan_img = ""
    if ttd_base64.strip() != "":
        ttd_data = base64.b64decode(ttd_base64.split(",")[1])
        with open("tanda_tangan.png", "wb") as f:
            f.write(ttd_data)
        tanda_tangan_img = InlineImage(doc, "tanda_tangan.png", width=Inches(1.5))

    # Fungsi untuk mengubah format tanggal ke 'hari bulan tahun' (contoh: 30 September 2025)
    def format_tanggal(tanggal_str):
        bulan_id = [
            '', 'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
            'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'
        ]
        try:
            # Coba parsing tanggal dalam format YYYY-MM-DD
            dt = datetime.strptime(tanggal_str, '%Y-%m-%d')
            return f"{dt.day} {bulan_id[dt.month]} {dt.year}"
        except Exception:
            return tanggal_str  # fallback jika format tidak sesuai

    context = {
        "nama": nama,
        "npm": npm,
        "program": program,
        "instansi": instansi,
        "matakul": matakul,
        "dosen": dosen,
        "kelas": kelas,
        "pertemuan": pertemuan,
        "tanggal": format_tanggal(tanggal),
        "alasan": alasan,
        "tanggal_surat": format_tanggal(tanggal_surat),
        "tanda_tangan": tanda_tangan_img
    }

    doc.render(context)
    filename_docx = f"surat_izin_{npm}_{int(time.time())}.docx"
    doc.save(filename_docx)

    # Convert DOCX to PDF using LibreOffice (soffice) dengan path absolut dan log error
    filename_pdf = filename_docx.replace(".docx", ".pdf")
    abs_docx = os.path.abspath(filename_docx)
    outdir = os.path.dirname(abs_docx)
    try:
        subprocess.run([
            "soffice", "--headless", "--convert-to", "pdf", abs_docx, "--outdir", outdir
        ], check=True)
        last_pdf = filename_pdf
    except Exception as e:
        print("Gagal konversi PDF:", e)
        last_pdf = filename_docx  # fallback to docx if conversion fails

    return redirect(url_for("preview"))

@app.route("/preview")
def preview():
    global last_pdf
    if last_pdf and os.path.exists(last_pdf):
        return send_file(last_pdf, as_attachment=True)
    return "Belum ada file yang dihasilkan."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

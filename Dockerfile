FROM python:3.10-slim

# Install LibreOffice dan dependensi
RUN apt-get update && apt-get install -y libreoffice python3-pip && apt-get clean

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "program:app", "--bind", "0.0.0.0:${PORT:-8080}"]

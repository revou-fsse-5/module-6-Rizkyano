# Menggunakan image resmi Python sebagai base image
FROM python:3.12

# Set working directory
WORKDIR /app

# Menyalin file pyproject.toml dan poetry.lock
COPY pyproject.toml poetry.lock /app/

# Menginstal Poetry
RUN pip install poetry

# Menginstal dependensi tanpa menginstal package root
RUN poetry install --no-root

# Menyalin seluruh kode aplikasi ke dalam container
COPY . /app

# Menetapkan variabel environment
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Menjalankan aplikasi Flask
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

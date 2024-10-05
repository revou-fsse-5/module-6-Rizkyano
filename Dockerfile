# Gunakan image dasar Python 3.9
FROM python:3.12.5

# Tentukan working directory di dalam container
WORKDIR /app

# Copy semua file ke dalam working directory
COPY . /app

# Install dependencies menggunakan pip (flask, dll.)
RUN pip install flask

RUN pip install poetry

RUN poetry install --no-root
# Expose port 5000 (port default Flask)
EXPOSE 5000

# Command untuk menjalankan aplikasi Flask
CMD ["flask", "run", "--host=0.0.0.0"]

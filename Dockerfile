FROM python:3.12-slim

WORKDIR /app

# Devido ao webscrap torna se necessario usar um emulador do navegador
RUN apt-get update && \
    apt-get install -y wget unzip chromium-driver chromium

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]




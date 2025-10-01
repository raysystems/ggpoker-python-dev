FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y chromium-driver chromium libnss3 libatk1.0-0 libx11-xcb1 libxcomposite1 libxrandr2 libxdamage1 libxkbcommon0 libgbm1 libpango-1.0-0 libcups2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
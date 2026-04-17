FROM python:3.12-slim

WORKDIR /app

# системные зависимости (если вдруг нужны либы для пакетов)
RUN apt-get update && apt-get install -y curl gcc && rm -rf /var/lib/apt/lists/*

# зависимости Python
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# копируем весь проект
COPY . .

# чтобы pytest мог писать отчёты/логи
VOLUME ["/app/logs"]

# дефолтный запуск тестов
CMD ["pytest", "-s", "-v"]
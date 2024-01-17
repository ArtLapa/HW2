# Використовуємо базовий образ Python
FROM python:3.8

# Копіюємо файли проекту в контейнер
COPY . /app

# Переходимо в робочу директорію
WORKDIR /app

# Встановлюємо залежності через poetry
RUN pip install poetry && poetry install

# Виконуємо вашу програму при старті контейнера
CMD ["python", "your_main_script.py"]

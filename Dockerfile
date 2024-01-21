# Використовуємо базовий образ Python версії 3.11
FROM python:3.11

# Створюємо робочу директорію /app в контейнері
WORKDIR /app

# Копіюємо файли проекту в контейнер
COPY . .

# Встановлюємо poetry
RUN pip install poetry

# Встановлюємо залежності за допомогою poetry
RUN poetry install

# Запускаємо ваш основний скрипт Helpi.py, припускаючи, що він знаходиться в папці "HM2"
CMD ["python", "HM2/Helpi.py"]



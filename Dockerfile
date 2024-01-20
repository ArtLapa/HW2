FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry install

CMD ["python", "HW2/Helpi.py"]


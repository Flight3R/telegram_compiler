FROM python:3.8-slim

WORKDIR /telegram_compiler
COPY src /telegram_compiler

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]

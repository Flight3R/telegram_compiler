FROM python:3.12-slim

WORKDIR /telegram_compiler
COPY src /telegram_compiler

RUN apt-get update && \
    apt-get -y install g++
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt install g++ -y

CMD ["python", "main.py"]

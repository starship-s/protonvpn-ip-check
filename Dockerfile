#Contents of Dockerfile
FROM python:3.11-slim

RUN apt-get update

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade pip setuptools && \
    pip3 install --no-cache-dir -r requirements.txt

# bring across python scripts
COPY . .

ENTRYPOINT ["python3", "-u", "app.py"]
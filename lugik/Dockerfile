FROM python:3.6.1-slim

WORKDIR /lugik

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
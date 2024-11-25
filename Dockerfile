FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y \
    unixodbc-dev \
    gcc \
    g++ \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
    

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
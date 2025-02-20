FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    make \
    vim \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    tap-mysql \
    singer-target-postgres

WORKDIR /app

COPY . .

CMD ["bash"]

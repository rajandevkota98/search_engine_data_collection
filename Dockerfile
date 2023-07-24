FROM python:3.9.14-slim-bullseye

COPY . /search_engine_data_collection

WORKDIR /search_engine_data_collection

RUN apt-get update \
    && apt-get install -y gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8081

CMD ["python","app.py"]
FROM python:3.12.0

RUN pip install pandas sqlalchemy psycopg2-binary requests pyarrow

WORKDIR /app

COPY ingest_data.py .

CMD ["python", "ingest_data.py"]
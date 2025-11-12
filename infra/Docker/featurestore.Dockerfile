FROM python:3.11-slim-bullseye

WORKDIR /app
COPY ./featurestore/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./featurestore .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

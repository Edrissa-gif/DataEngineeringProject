.PHONY: up down build init-db ingest etl

up:
	docker compose up -d --build

down:
	docker compose down

build:
	docker compose build

init-db:
	docker exec -i de_postgres psql -U ${POSTGRES_USER} -d ${POSTGRES_DB} < metadata/init_db.sql

ingest:
	docker exec ingestion python /app/ingestion/app.py

etl:
	docker exec spark-master spark-submit --master spark://spark-master:7077 /opt/spark/jobs/etl_job.py

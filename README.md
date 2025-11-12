

## Overview

This project implements a **batch-processing data architecture** designed to support a data-intensive machine learning application. It demonstrates a reliable, scalable, and maintainable data pipeline, including:

- **Data ingestion**: Generates and ingests large-scale, time-stamped transaction data.  
- **ETL and aggregation**: Processes raw data using Apache Spark.  
- **Feature store**: Stores aggregated features for downstream ML use.  
- **Orchestration**: Uses Apache Airflow to schedule batch processing pipelines.  
- **Containerization**: Docker-based microservices for isolated and reproducible deployment.

> Note: This project demonstrates the **development phase**. Finalization will include enhanced storage, API endpoints, logging, error handling, and security improvements.

---

## Project Structure

```

├── AirFlow/                  # Airflow DAGs and requirements
│   ├── Dockerfile
│   ├── batch_pipeline_dag.py
│   └── requirements.txt
├── configs/                  # Configurations for services
│   └── minio/
│       └── spark/
├── docker-compose.yml        # Docker Compose orchestration
├── featurestore/             # Feature store microservice
│   ├── app.py
│   └── requirements.txt
├── infra/Docker/             # Dockerfiles for all microservices
│   ├── featurestore.Dockerfile
│   ├── ingestion.Dockerfile
│   └── spark.Dockerfile
├── ingestion/                # Data ingestion microservice
│   ├── app.py
│   ├── generate_data.py
│   ├── requirements.txt
│   └── sample_data/transactions.csv
├── metadata/                 # Database initialization and migrations
│   ├── init_db.sql
│   └── migrations/
├── spark_jobs/               # Spark ETL jobs
│   ├── etl_job.py
│   └── requirements.txt
├── Makefile                  # For executing common tasks
└── README.md

````

---

## Prerequisites

- **Docker & Docker Compose** (to run services locally)  
- **Python 3.11+** (for running microservices locally if needed)  
- **Apache Spark** (optional if running ETL locally instead of containerized)  

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Edrissa-gif/DataEngineeringProject.git
cd DataEngineeringProject
````

2. **Set up environment variables**

```bash
cp .env.example .env
# Edit .env with credentials or paths if needed
```

3. **Build and start services using Docker Compose**

```bash
docker-compose up --build
```

4. **Access Airflow UI**
   Open `http://localhost:8080` to monitor DAGs and schedule batch pipelines.

---

## Usage

### 1. Data Ingestion

* Generates synthetic transaction data and stores it locally.

```bash
python ingestion/generate_data.py
```

### 2. ETL with Spark

* Processes raw data into aggregated features.

```bash
python spark_jobs/etl_job.py
```

### 3. Feature Store

* Stores processed features for ML consumption (future API endpoints to be added in finalization phase).

```bash
docker build -t featurestore ./infra/Docker -f featurestore.Dockerfile
docker run -p 5000:5000 featurestore
```

### 4. Airflow Batch Pipeline

* Automates ingestion → ETL → feature store workflow.
* DAG currently scheduled manually for demonstration; will be set to quarterly batch processing in finalization phase.

---

## Key Features

* Fully **Dockerized microservices** for isolated and reproducible deployment.
* **Apache Spark** for scalable ETL processing.
* **Airflow DAGs** for orchestration of batch workflows.
* Modular project structure ready for future enhancements:

  * Persistent storage (MinIO/database)
  * Feature delivery API
  * Logging, retries, error handling
  * Security and governance

---

## Next Steps / Finalization Phase

* Implement **data persistence** for raw and processed data.
* Add **REST API endpoints** for feature delivery to ML models.
* Improve **reliability** with logging, error handling, and retries.
* Enhance **security** and governance.
* Define **explicit batch scheduling** in Airflow DAG.
* Write reflection and lessons learned for project completion.

---






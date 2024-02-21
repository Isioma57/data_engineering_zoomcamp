# Data Engineering Zoomcamp

This repository contains notes and codes from DataTalks [Data Engineering zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)

## Modules

### 1. Introduction and Prerequisites
This section covers the essentials of Docker, including the deployment of PostgreSQL and pgAdmin containers via Docker Compose. It also touches on fundamental SQL concepts and the configuration of cloud infrastructure on Google Cloud through Terraform.

#### 📗Resources
- [Module](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform) 
- [Homework](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/01-docker-terraform/homework.md)

#### 📺 Videos
- [**1**: Introduction to Docker](https://www.youtube.com/watch?v=EYNwNlOrpr0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=4)
- [**2**: Ingesting NY Taxi Data to Postgres](https://www.youtube.com/watch?v=2JM-ziJt0WI&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=5) 
- [**3**: Connecting pgAdmin and Postgres](https://www.youtube.com/watch?v=hCAIVe9N0ow&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=7)
- [**4**: Dockerizing the Ingestion Script](https://www.youtube.com/watch?v=B1WwATwf-vY&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=8)
- [**5**: Running Postgres and pgAdmin with Docker-Compose](https://www.youtube.com/watch?v=hKI6PkPhpa0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=9)
- [**6**: SQL Refreshser](https://www.youtube.com/watch?v=QEcps_iskgg&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=10) 
- [**7**: Terraform Primer](https://www.youtube.com/watch?v=s2bOYDCKl_M&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=11)
- [**8**: Terraform Basics](https://www.youtube.com/watch?v=Y2ux7gq3Z0o&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=12)
- [**9**: Terraform Variables](https://www.youtube.com/watch?v=PBi0hHjLftk&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=13)

#### Environment setup 

For the course you'll need:

* Python 3 (e.g. installed with Anaconda)
* Google Cloud SDK
* Docker with docker-compose
* Terraform
* Git account

### 📚My Notes

[PostgreSQL with Docker: From Setup to Data Ingestion and pgAdmin Integration](https://blog.devops.dev/postgresql-with-docker-from-setup-to-data-ingestion-and-pgadmin-integration-929c966cc650)

[Practical Steps to Streamline PostgreSQL and pgAdmin Deployment with Docker Compose](https://blog.devops.dev/practical-steps-to-streamline-postgresql-and-pgadmin-deployment-with-docker-compose-6ac74a0808df)

[Terraform](https://github.com/Isioma57/data_engineering_zoomcamp/blob/main/modules/1.%20Intro_%26_Prerequisites/Terraform/README.md)


### 2. WorkFlow Orchestration

This section covers workflow orchestration with mage. Mage is an open-source, hybrid framework for transforming and integrating data.

#### 📺 Videos


* [2.2.1 - Intro to Orchestration](#221----intro-to-orchestration)
* [2.2.2 - Intro to Mage](#222---%EF%B8%8F-intro-to-mage)
* [2.2.3 - ETL: API to Postgres](#223----etl-api-to-postgres)
* [2.2.4 - ETL: API to GCS](#224----etl-api-to-gcs)
* [2.2.5 - ETL: GCS to BigQuery](#225----etl-gcs-to-bigquery)
* [2.2.6 - 👨Parameterized Execution](#226----parameterized-execution)
* [2.2.7 - Deployment (Optional)](#227----deployment-optional)
* [2.2.8 - Homework](#228---️-homework)

#### 📗Resources

- [Slides](https://docs.google.com/presentation/d/1yN-e22VNwezmPfKrZkgXQVrX5owDb285I2HxHWgmAEQ/edit#slide=id.g262fb0d2905_0_12)
- [Mage Docs](https://docs.mage.ai/)
- [Mage Guides](https://docs.mage.ai/guides)
- [Mage Slack](https://www.mage.ai/chat)

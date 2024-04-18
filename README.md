# Virginia School Accredition based on SOL passrates

## 1. Description of the problem

Public education is free and appropriate for all bodies from kindergarten age to 12th grade level.  Ever since Covid shut down the world in 2020, the education system has been under fire even more so due to students losing at least a year of learning while still being pushed forward with the expectation that those students are on pace with the learning curriculum for the new current grade or subject.  With the school systems in Virginia, [the VDOE website](https://www.doe.virginia.gov/data-policy-funding/data-reports/statistics-reports/sol-test-pass-rates-other-results) has a gap of data for the school year of 2020-2021 thus, a reset has been established.  With the setbacks, how do the schools, throughout the state, stand on the level of accreditation solely based upon SOL pass rates?


## 2. Data Architecture

I created a data architure flow for the Data Engineering Zoomcamp 2024.  This flows is for a batching processing.
![data architecture](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Screenshot%202024-04-18%20011918.png)


## 3. Objective

The goal of this project was to build an end-to-end data pipeline.  First setup a VM that can run Anaconda Python and can be accessed with an SSH key.  Then create a BigQuery project through the Google Console that will store the data. This will require a policy role that allows access to read/write access to BigQuery.  Followed by creating a DBT project within the DBT Cloud that connects to the BigQuery using the role that was created to access read/write access to BigQuery.  A GitHub repository will also need to be created.  Connect the GitHub account to DBT and port over the files and folders for the DBT execution. Finally use Looker Studio and connect it to the google console and give it access to the integrated dataset to create dashboards.

## 3.Technology Used

The technology used for the project are as follows:
* __Data Lake__: [Google Cloud Platform(GCP)](https://cloud.google.com/?hl=en)
* __Integrated Development Environment(IDE)__: [Python](https://www.python.org/)
* __Data Warehouse__: [Big Query](https://cloud.google.com/bigquery?_gl=1*ix9b2*_up*MQ..&gclid=CjwKCAjw5v2wBhBrEiwAXDDoJaGHHWiJhQYvl7sPTiJiaOPTcGyKB6KO2E0f43divUy7t6hBgMUWsRoCzVAQAvD_BwE&gclsrc=aw.ds#from-cloud-data-warehouse-to-an-ai-ready-data-platform)
* __Transformations__: [Data Build Tool (DBT)](https://www.getdbt.com/)
* __Repositiory__: [GitHub](https://github.com/)
* __Visulization__: [Looker Studio](https://lookerstudio.google.com/)


## 4. Setup

The goal of this project was to build an end-to-end data pipeline.  First setup a VM that can run Anaconda Python and can be accessed with an SSH key.  Then create a BigQuery project through the Google Console that will store the data. This will require a policy role that allows access to read/write access to BigQuery.  Followed by creating a DBT project within the DBT Cloud that connects to the BigQuery using the role that was created to access read/write access to BigQuery.  A GitHub repository will also need to be created.  Connect the GitHub account to DBT and port over the files and folders for the DBT execution. Finally use Looker Studio and connect it to the google console and give it access to the integrated dataset to create dashboards.

## 5. Dashboard

!(dashboard)[Screenshot 2024-04-18 021244.png]

## 6. Reproducibility








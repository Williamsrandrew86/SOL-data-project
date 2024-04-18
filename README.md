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
 - __Data Lake__: [Google Cloud Platform(GCP)](https://cloud.google.com/?hl=en)
 - __Integrated Development Environment(IDE)__: [Python](https://www.python.org/)
 - __Data Warehouse__: [Big Query](https://cloud.google.com/bigquery?_gl=1*ix9b2*_up*MQ..&gclid=CjwKCAjw5v2wBhBrEiwAXDDoJaGHHWiJhQYvl7sPTiJiaOPTcGyKB6KO2E0f43divUy7t6hBgMUWsRoCzVAQAvD_BwE&gclsrc=aw.ds#from-cloud-data-warehouse-to-an-ai-ready-data-platform)
 - __Transformations__: [Data Build Tool (DBT)](https://www.getdbt.com/)
 - __Repositiory__: [GitHub](https://github.com/)
 - __Visulization__: [Looker Studio](https://lookerstudio.google.com/)


## 4. Setup

The goal of this project was to build an end-to-end data pipeline.  First setup a VM that can run Anaconda Python and can be accessed with an SSH key.  Then create a BigQuery project through the Google Console that will store the data. This will require a policy role that allows access to read/write access to BigQuery.  Followed by creating a DBT project within the DBT Cloud that connects to the BigQuery using the role that was created to access read/write access to BigQuery.  A GitHub repository will also need to be created.  Connect the GitHub account to DBT and port over the files and folders for the DBT execution. Finally use Looker Studio and connect it to the google console and give it access to the integrated dataset to create dashboards.

## 5. Dashboard

![dashboard](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Screenshot%202024-04-18%20021244.png)
[dashboard](https://lookerstudio.google.com/s/hdFwzPT_GC0)

## 6. Reproducibility

## Virtual Machine Setup

1. **Anaconda Python Installation:**
   - Install Anaconda Python on the VM to manage packages and environments efficiently.

2. **VS Code Installation with SSH Extension:**
   - Install Visual Studio Code (VS Code) on your personal computer.
   - Enable the SSH extension in VS Code and ensure it's configured to work under the `.ssh` folder for remote development.

3. **SSH Key Configuration:**
   - Generate an SSH key pair on your personal computer.
   - Add the public key to the VM's metadata settings to establish secure SSH connections.
![Virtual Machine is up and running](
## BigQuery Setup

1. **Project Creation:**
   - Create a new project in BigQuery through the Google Cloud Console.

2. **Dataset Creation:**
   - Within the project, create a dataset named `sol_data` to store the project's data.

3. **Role Configuration:**
   - Set up a custom role in the Google Cloud Console that grants read/write access to BigQuery.

## DBT Setup

1. **DBT Project Creation:**
   - Create a new project within DBT Cloud for data transformation tasks.

2. **BigQuery Connection:**
   - Connect DBT to BigQuery using the custom role created earlier with read/write access.

3. **GitHub Repository Creation:**
   - Create a new GitHub repository to hold the results of DBT transformations.

4. **GitHub Integration:**
   - Grant access to the GitHub repository to DBT for seamless integration.
   - Transfer necessary files and folders for DBT execution to the repository.

## Project Execution

1. **Python Script Execution:**
   - Run a Python script on the VM to pull data from a GitHub source to BigQuery.
   - Ensure the script references the correct SSH key and folder location for the BigQuery role.
   - Update the project ID in the script with your specific project ID.

2. **DBT Script Execution:**
   - Execute DBT scripts to create an integrated dataset based on the transformed data.

3. **Scheduled Execution (Optional):**
   - Schedule the script to run daily, simulating a daily data integration process.

## Looker Setup

1. **Looker Studio Connection:**
   - Connect Looker to your Google Cloud project.
   - Grant Looker access to the integrated dataset for visualization and analysis.







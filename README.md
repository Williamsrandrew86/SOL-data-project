# Virginia School Accredition based on SOL pass rates

## 1. Description of the problem

Public education is free and appropriate for all bodies from kindergarten age to 12th grade level.  Ever since Covid shut down the world in 2020, the education system has been under fire even more so due to students losing at least a year of learning while still being pushed forward with the expectation that those students are on pace with the learning curriculum for the new current grade or subject.

With the school systems in Virginia, [the VDOE website](https://www.doe.virginia.gov/data-policy-funding/data-reports/statistics-reports/sol-test-pass-rates-other-results) has a gap of data for the school year of 2020-2021 thus, a reset has been established.  With the setbacks, how do the schools, throughout the state, stand on the level of accreditation solely based upon SOL pass rates?


## 2. Data Architecture

I created a data architure flow for the Data Engineering Zoomcamp 2024.

![data architecture](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/dataArchitecture.png)

### Architecture Components

The source data is located in a github repository for public and easy access. The first Python block:

- Imports the data
- Drops unused columns
- Deals with messy columns to convert them to numeric
- Adds -9999 for null values as an error code.
- Pushes the data to two separate raw files in BigQuery

The DBT process:

- Pulls the data from BigQuery
- Innerjoin the two dataframes
- Created two columns for Pass_Fail_(year)
- Push the dataframe back to BigQuery

Looker Studio:

- Connected Looker Studio to BigQuery
- Uploaded the data into Looker Studio
- Created interactive Dashboards



## 3.Technology Used

The technology used for the project are as follows:
 - __Data Lake__: [Google Cloud Platform(GCP)](https://cloud.google.com/?hl=en)
 - __Integrated Development Environment(IDE)__: [Python](https://www.python.org/)
 - __Data Warehouse__: [Big Query](https://cloud.google.com/bigquery?_gl=1*ix9b2*_up*MQ..&gclid=CjwKCAjw5v2wBhBrEiwAXDDoJaGHHWiJhQYvl7sPTiJiaOPTcGyKB6KO2E0f43divUy7t6hBgMUWsRoCzVAQAvD_BwE&gclsrc=aw.ds#from-cloud-data-warehouse-to-an-ai-ready-data-platform)
 - __Transformations__: [Data Build Tool (DBT)](https://www.getdbt.com/)
 - __Repositiory__: [GitHub](https://github.com/)
 - __Visulization__: [Looker Studio](https://lookerstudio.google.com/)

## 4 Dashboard

![dashboard](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/dashboard.png)
[dashboard](https://lookerstudio.google.com/s/hdFwzPT_GC0)

## 5. Reproducibility

## Virtual Machine

1. **Anaconda Python Installation:**
   - Install Anaconda Python on the VM to manage packages and environments efficiently.

2. **VS Code Installation with SSH Extension:**
   - Install Visual Studio Code (VS Code) on your personal computer.
   - Enable the SSH extension in VS Code and ensure it's configured to work under the `.ssh` folder for remote development.

3. **SSH Key Configuration:**
   - Generate an SSH key pair on your personal computer.
   - Add the public key to the VM's metadata settings to establish secure SSH connections.
     ![sshconnetionmade](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/sshlogin.png)
     
4. **Start the jupyter notebook**
   - Copy and paste the local host into the address bar
     ![gitbash photo here](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/login%20notebook.png)

5. **Upload the data**
   - Create a new notebook
   - Upload the following libraries
     -  ![libraries](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/library.png)
   - Upload the data to create two data frames from the repositiory
     - ![photo of data](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/data%20pull.png)
   - Transformation done to each data frame (make sure you repeat for both data frames)
     - Drop columns that were not needed
       ![drop](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/drop%20column.png)
     - Replace the ' ' and '-' with '_' in all column names
       ![name change](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/mod%20column%20names.png)
     - Modify data within columns
       - Replace '<' with '-9999'
       - Change nan with 'None'
       - Change data type to int
         ![modify data](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/change%20values.png)
   
       
## BigQuery

1. **Project Creation:**
   - Create a new project in BigQuery through the Google Cloud Console.
     
     ![new project](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/adddatadet.png)
     
2. **Dataset Creation:**
   - Within the project, create a dataset named `sol_data` to store the project's data.
     
     ![dataset create](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/createdataset.png)
     
3. **Role Configuration:**
   - Set up a custom role in the Google Cloud Console that grants read/write access to BigQuery.
     
     ![environment link](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/IAM.png)
     ![keys](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/keys.png)

 4. **Data Frame pushed into BigQuery**
   - Write code that accesses BidQuery and create tables in the 'sol_data'
      - Environment key to BigQuery
        
        ![Enviroment](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/enviroment.png)
        
      - Create tables in BigQuery(make sure you repeat create_or_append for all data frames)

        ![tablecreate](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/table%20create.png)

## DBT

1. **DBT Project Creation:**
   - Create a new project within DBT Cloud for data transformation tasks.

2. **BigQuery Connection:**
   - Connect DBT to BigQuery using the custom role created earlier with read/write access.

3. **GitHub Repository Creation:**
   - Create a new GitHub repository to hold the results of DBT transformations.

4. **GitHub Integration:**
   - Grant access to the GitHub repository to DBT for seamless integration.
   - Transfer necessary files and folders for DBT execution to the repository.

5. **Create SQL case**
   - Configure a table

     ![configtable](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/configtable.png)

   - Transformation
     - Inner join the dataframes
     - Create two columns "Pass_Fail_(year)" that look at pass_rate and fill the column with the correct value that met the condition
     - If the score was below a 70 then it was considered a Fail, Pass if above 70 and Null if the data was missing

     ![sqlcode](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/sqlcode.png)
     
## Schedule Execution
   - Schedule the script to run yearly around September.  The SOL scores are updated yearly on the VDOE website.

## Looker Setup

1. **Looker Studio Connection:**
   - Connect Looker to your Google Cloud project.
  
     ![lookerstart](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/lookerstudiolink.png)

   - Add the data to Lookerstudio
  
     ![lookerdata](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/lookerdata.png)

 2. **Create an interactive Dashboard**
    - Drag your data into the fields and make adjustment as needed to create a visual you desire to see
   
      ![lookerdash](https://github.com/Williamsrandrew86/SOL-data-project/blob/main/Images/lookerdash.png)







import pyspark
import pandas as pd
import os
from google.cloud import bigquery
from pyspark.sql import SparkSession
from pyspark.sql import types
from pyspark.sql import functions as f

#  pip install google-cloud-bigquery

df_2023 = pd.read_csv('https://raw.githubusercontent.com/Williamsrandrew86/SOL-data-project/main/data/school_pass_rates_by_test_2022_2023.csv')

mod_df_2023 = df_2023.drop(['2020-2021 Pass Rate','2021-2022 Pass Rate','2020-2021 Adv Pass Rate','2021-2022 Adv Pass Rate'], axis=1)

mod_df_2023.columns = mod_df_2023.columns.str.replace(' ', '_') #change the spaces with underscores
mod_df_2023.columns = mod_df_2023.columns.str.replace('-', '_') #change the hypens with underscores

columns_to_replace = ['High_Grade'] # Specify columns to replace NaN with -9999

mod_df_2023[columns_to_replace] = mod_df_2023[columns_to_replace].fillna(value=-9999)# Replace NaN values with -9999 for specific columnsd

columns_to_replace = ['Low_Grade']# Specify columns to replace NaN with -9999

mod_df_2023[columns_to_replace] = mod_df_2023[columns_to_replace].fillna(value='None')# Replace NaN values with None for specific columns

mod_df_2023['2022_2023_Adv_Pass_Rate'] = mod_df_2023['2022_2023_Adv_Pass_Rate'].str.replace('<', '-9999')
mod_df_2023['2022_2023_Adv_Pass_Rate'] = mod_df_2023['2022_2023_Adv_Pass_Rate'].fillna(value='-9999')
mod_df_2023['2022_2023_Pass_Rate'] = mod_df_2023['2022_2023_Pass_Rate'].str.replace('<', '-9999')
mod_df_2023['2022_2023_Pass_Rate'] = mod_df_2023['2022_2023_Pass_Rate'].fillna(value='-9999')
mod_df_2023['2022_2023_Pass_Rate'].unique()
mod_df_2023['2022_2023_Pass_Rate'] = pd.to_numeric(mod_df_2023['2022_2023_Pass_Rate'], errors='coerce').astype('int')
mod_df_2023['2022_2023_Adv_Pass_Rate'] = pd.to_numeric(mod_df_2023['2022_2023_Adv_Pass_Rate'], errors='coerce').astype('int')

df_2022 = pd.read_csv('https://raw.githubusercontent.com/Williamsrandrew86/SOL-data-project/main/data/school-by-test-2022.csv')

mod_df_2022 = df_2022.drop(['2019-2020 Pass Rate','2020-2021 Pass Rate','2019-2020 Adv Pass Rate','2020-2021 Adv Pass Rate'], axis=1)

mod_df_2022.columns = mod_df_2022.columns.str.replace(' ', '_') #change the spaces with underscores
mod_df_2022.columns = mod_df_2022.columns.str.replace('-', '_') #change the hypens with underscores

columns_to_replace = ['High_Grade']# Specify columns to replace NaN with -9999

mod_df_2022[columns_to_replace] = mod_df_2022[columns_to_replace].fillna(value=-9999)# Replace NaN values with -9999 for specific columnsd

columns_to_replace = ['Low_Grade']# Specify columns to replace NaN with -9999

mod_df_2022[columns_to_replace] = mod_df_2022[columns_to_replace].fillna(value='None')# Replace NaN values with None for specific columns

mod_df_2022['2021_2022_Adv_Pass_Rate'] = mod_df_2022['2021_2022_Adv_Pass_Rate'].str.replace('<', '-9999')
mod_df_2022['2021_2022_Adv_Pass_Rate'] = mod_df_2022['2021_2022_Adv_Pass_Rate'].fillna(value='-9999')
mod_df_2022['2021_2022_Pass_Rate'] = mod_df_2022['2021_2022_Pass_Rate'].str.replace('<', '-9999')
mod_df_2022['2021_2022_Pass_Rate'] = mod_df_2022['2021_2022_Pass_Rate'].fillna(value='-9999')
mod_df_2022['2021_2022_Pass_Rate'].unique()
mod_df_2022['2021_2022_Pass_Rate'] = pd.to_numeric(mod_df_2022['2021_2022_Pass_Rate'], errors='coerce').astype('int')
mod_df_2022['2021_2022_Adv_Pass_Rate'] = pd.to_numeric(mod_df_2022['2021_2022_Adv_Pass_Rate'], errors='coerce').astype('int')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rwilliams/sol_data_project/sol_key.json"

client = bigquery.Client()

def create_or_append_table_in_bigquery(dataframe, project_id, dataset_id, table_id):
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    try:
        table = client.get_table(table_ref)
    except:
        print(f"Table {table_id} not found in dataset {dataset_id}, creating a new one.")
        schema = [
            bigquery.SchemaField('LEVEL', 'STRING'),
            bigquery.SchemaField('Div_Num', 'INTEGER'),
            bigquery.SchemaField('Div_Name', 'STRING'),
            bigquery.SchemaField('Sch_Num', 'INTEGER'),
            bigquery.SchemaField('Sch_Name', 'STRING'),
            bigquery.SchemaField('Sch_Type', 'STRING'),
            bigquery.SchemaField('Low_Grade', 'STRING'),
            bigquery.SchemaField('High_Grade', 'INTEGER'),
            bigquery.SchemaField('Subject', 'STRING'),
            bigquery.SchemaField('Grade', 'STRING'),
            bigquery.SchemaField('Test', 'STRING'),
            bigquery.SchemaField('2022_2023_Pass_Rate', 'INTEGER'),
            bigquery.SchemaField('2022_2023_Adv_Pass_Rate', 'INTEGER')
        ]
        table = bigquery.Table(table_ref)
        table = client.create_table(table)
        print(f"Created table {table.project}.{table.dataset_id}.{table.table_id}")

    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
    client.load_table_from_dataframe(dataframe, table_ref, job_config=job_config).result()

    create_or_append_table_in_bigquery(mod_df_2023, 'valiant-surfer-411804', 'sol_data', '2023_sol_data')

    create_or_append_table_in_bigquery(mod_df_2022, 'valiant-surfer-411804', 'sol_data', '2022_sol_data')

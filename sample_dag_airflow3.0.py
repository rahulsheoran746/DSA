from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta
from airflow.providers.amazon.aws.hooks.base_aws import AwsBaseHook
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'retries': 0,
    'retry_delay': timedelta(hours = 4)
}

# Fetch AWS credentials from Airflow Connections
aws_src_hook = AwsBaseHook(aws_conn_id='cdp_raw_us_b24_credentials_1', client_type='s3')
aws_source_credentials = aws_src_hook.get_credentials()

#Fetch snowflake credentials from Airflow Connections
snowflake_hook = SnowflakeHook(snowflake_conn_id='snowflake_cred')
conn = snowflake_hook.get_connection(snowflake_hook.snowflake_conn_id)

sf_username = conn.login
sf_password = conn.password


# Set environment variables for AWS credentials
env_var = {
    'SRC_AWS_ACCESS_KEY_ID': aws_source_credentials.access_key,
    'SRC_AWS_SECRET_ACCESS_KEY': aws_source_credentials.secret_key,
    "SNOWFLAKE_USER": sf_username,
    "SNOWFLAKE_PASSWORD": sf_password
}

# Define the DAG
with DAG(
    'incremental_doceree_accounts_dag',
    default_args=default_args,
    description='DHC tables updation dag for doceree accounts.',
    schedule_interval='30 5 * * 1',
    start_date=datetime(2025, 6, 19),
    catchup=False
) as dag:

    # SparkSubmitOperator to run the Spark job
    spark_submit_task = SparkSubmitOperator(
        task_id='spark_submit_task',
        application='/home/airflow/dags/code/incremental_doceree_accounts.py',
        conn_id='spark_default',
        conf={
            "spark.executor.instances": "30",
            'spark.cores.max': '58',
            'spark.executor.cores': '2',
            'spark.executor.memory': '10G',
            'spark.driver.memory': '20G',
            'spark.driver.cores': '4',
            'spark.executor.memoryOverhead': '2048M',
            'spark.driver.memoryOverhead': '2048M',
            'spark.sql.adaptive.enabled': 'true'
            # 'spark.serializer': 'org.apache.spark.serializer.KryoSerializer',
            # 'spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version': '2',
            # 'spark.hadoop.mapreduce.fileoutputcommitter.marksuccessfuljobs': 'true',
            # 'spark.hadoop.fs.s3a.checksum.enabled': 'true',
            # 'spark.driver.extraJavaOptions': '-XX:+UseG1GC -XX:MaxGCPauseMillis=500 -XX:+ParallelRefProcEnabled',
            # 'spark.executor.extraJavaOptions': '-XX:+UseG1GC -XX:MaxGCPauseMillis=500 -XX:+ParallelRefProcEnabled',
            # 'spark.task.maxFailures': '4',
            # 'spark.hadoop.fs.s3a.impl': 'org.apache.hadoop.fs.s3a.S3AFileSystem'
        },
        env_vars=env_var,
        packages="org.apache.hadoop:hadoop-aws:3.3.4,org.apache.spark:spark-hadoop-cloud_2.12:3.5.4,net.snowflake:snowflake-jdbc:3.13.6,net.snowflake:spark-snowflake_2.13:2.16.0-spark_3.4",
    )

    spark_submit_task 

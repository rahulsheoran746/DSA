from airflow import DAG
from airflow.providers.amazon.aws.sensors.emr import EmrStepSensor
from airflow.utils.trigger_rule import TriggerRule
from airflow.providers.amazon.aws.operators.emr import (
    EmrCreateJobFlowOperator,
    EmrAddStepsOperator,
    EmrTerminateJobFlowOperator
)
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(hours=5),
}

with DAG(
    dag_id='incremental_npi_join_adrequest_columns_dag',
    default_args=default_args,
    description='incremental_npi_join_adrequest_columns_dag.',
    schedule_interval='50 10 * * *',
    start_date=datetime(2025, 5, 12),
    catchup=False,
    tags=['emr', 'spark'],
) as dag:
    
    create_emr_cluster = EmrCreateJobFlowOperator(
        task_id='create_emr_cluster',
        aws_conn_id='aws_default',
        region_name='us-east-2',
        job_flow_overrides={
            'Name': 'incremental_npi_join_adrequest_columns_dag',
            'ReleaseLabel': 'emr-7.8.0',
            'Applications': [
                    {'Name': 'Spark'},
            ],
            'BootstrapActions': [
                {
                    'Name': 'Install dependencies',
                    'ScriptBootstrapAction': {
                        'Path': 's3://airflowcdp/dags/python-packages.sh'
                    }
                }
            ],
            'LogUri': 's3://airflowcdp/logs/',
            'Instances': {
                'InstanceGroups': [
                    {
                        'Name': "Master nodes",
                        'InstanceRole': 'MASTER',
                        'InstanceType': 'r7i.xlarge',
                        'InstanceCount': 1,
                    },
                    {
                        'Name': "Core nodes",
                        'InstanceRole': 'CORE',
                        'InstanceType': 'r7i.xlarge',
                        'InstanceCount': 3,
                    },
                    {
                        'Name': "Task nodes",
                        'InstanceRole': 'TASK',
                        'InstanceType': 'r7i.xlarge',
                        'InstanceCount': 1,
                    }
                ],
                'KeepJobFlowAliveWhenNoSteps': False,
                'TerminationProtected': False,
                'Ec2SubnetId': 'subnet-099163913d15cd436',
                'EmrManagedMasterSecurityGroup': 'sg-0d1d47e7119de0393',
                'EmrManagedSlaveSecurityGroup': 'sg-0d1d47e7119de0393' 
            },
            'JobFlowRole': 'EMR_EC2_DefaultRole',
            'ServiceRole': 'EMR_DefaultRole',
        },
    )

    emr_job_steps = [
        {
            'Name': 'incremental_npi_join_adrequest_columns_dag',
            'ActionOnFailure': 'CONTINUE',
            'HadoopJarStep': {
                'Jar': 'command-runner.jar',
                'Args': [
                    'spark-submit',
                    '--num-executors', '10',
                    '--packages', 'org.apache.hadoop:hadoop-aws:3.3.4,org.apache.spark:spark-hadoop-cloud_2.12:3.3.1,net.snowflake:snowflake-jdbc:3.24.2,net.snowflake:spark-snowflake_2.12:3.0.0',         
                    '--conf', 'spark.dynamicAllocation.enabled=false',
                    '--conf', 'spark.cores.max=20',
                    '--conf', 'spark.executor.memory=10G',
                    '--conf', 'spark.driver.memory=20G',
                    '--conf', 'spark.executor.cores=2',
                    '--conf', 'spark.driver.cores=4',
                    '--conf', 'spark.executor.memoryOverhead=2048',
                    '--conf', 'spark.driver.memoryOverhead=2048',
                    '--conf', 'spark.sql.adaptive.enabled=true',
                    's3://airflowcdp/code/incremental_npi_join_adrequest_columns.py'
                ]
            }
        }
    ]


    add_emr_job_steps = EmrAddStepsOperator(
        task_id='add_emr_job_steps',
        aws_conn_id='aws_default',
        job_flow_id=create_emr_cluster.output,
        steps=emr_job_steps,        
    )

    watch_emr_job_steps = EmrStepSensor(
        task_id='watch_emr_job',
        aws_conn_id='aws_default',
        job_flow_id=create_emr_cluster.output,
        step_id="{{ ti.xcom_pull(task_ids='add_emr_job_steps', key='return_value')[0] }}",
    )

    terminate_emr_cluster = EmrTerminateJobFlowOperator(
        task_id='terminate_emr_cluster',
        aws_conn_id='aws_default',
        job_flow_id=create_emr_cluster.output,
    )


    notify_failure = EmailOperator(
        task_id='send_failure_email',
        to=['nishant.gupta@doceree.com'],
        subject='[Airflow] DAG {{ dag.dag_id }} Failed',
        html_content="""
          <h3>Airflow DAG Failure</h3>
          <p><strong>DAG:</strong> {{ dag.dag_id }}</p>
          <p><strong>Task:</strong> {{ ti.task_id }}</p>
          <p><strong>Execution Time:</strong> {{ (execution_date + macros.timedelta(hours=5, minutes=30)).isoformat() }}</p>
        """,
        trigger_rule=TriggerRule.ONE_FAILED,
    )

    notify_success = EmailOperator(
        task_id='send_success_email',
        to=['nishant.gupta@doceree.com'],
        subject='[Airflow] DAG {{ dag.dag_id }} Succeeded',
        html_content="""
          <h3>Airflow DAG Succeeded</h3>
          <p><strong>DAG:</strong> {{ dag.dag_id }}</p>
          <p><strong>Execution Date:</strong> {{ (execution_date + macros.timedelta(hours=5, minutes=30)).isoformat() }}</p>
        """,
        trigger_rule=TriggerRule.ALL_SUCCESS,
    )

    create_emr_cluster >> add_emr_job_steps >> watch_emr_job_steps >> terminate_emr_cluster

    [create_emr_cluster, add_emr_job_steps, watch_emr_job_steps, terminate_emr_cluster] >> notify_failure
    terminate_emr_cluster >> notify_success
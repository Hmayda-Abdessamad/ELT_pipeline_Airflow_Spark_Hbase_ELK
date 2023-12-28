# Automated-Big-Data-Visualization-Pipeline-using-Apache-Airflow-and-ELK-Stack
Purpose: The project aims to automate the collection, processing, and visualization of financial data, enabling users to gain insights and make informed decisions based on the analyzed data. By integrating multiple technologies like Apache Airflow, Spark, HBase, Elasticsearch, and Kibana,

# Requirements

To run this project locally, ensure you have the following installed:

1) Docker
2) Python
   
# Procject's Architecture
![image](https://github.com/kadirimeriem/ELT_pipeline_Airflow_Spark_Hbase_ELK/assets/110923887/69b9d68b-bc34-48b7-b07e-8fb239be42e4)

# Project's  Workflow 

![image](https://github.com/kadirimeriem/ELT_pipeline_Airflow_Spark_Hbase_ELK/assets/110923887/1a8c7fc0-099b-43fd-adae-464f785fba5f)

# Running the Project Locally

Follow these steps to set up and run the project on your local machine:
1) Clone the Project and Navigate to Project Folder:
git clone [https://github.com/your/repository.git](https://github.com/Hmayda-Abdessamad/Automated-Big-Data-Visualization-Pipeline-using-Apache-Airflow-and-ELK-Stack.git)
cd Automated-Big-Data-Visualization-Pipeline-using-Apache-Airflow-and-ELK-Stack


2) Initialize Apache Airflow with Docker Compose:
   
a- Start the initialization of Apache Airflow by running:
docker-compose up airflow-init

b-Run Docker Compose:Once the initialization is complete, execute the following command to launch the project:
docker-compose up

3)-Access Airflow UI:
After successful execution, navigate to localhost:8080 in your web browser to access the Airflow UI. Here, you can monitor and manage the automated big data visualization pipeline.

# After running the project 

To acces to  
•	HBase : http://localhost:16010
![image](https://github.com/kadirimeriem/ELT_pipeline_Airflow_Spark_Hbase_ELK/assets/110923887/34e76fbd-2128-42b9-92a6-4aa2d81c9d86)

•	Spark : http://localhost:8081
•	Airflow : http://localhost:8080
Here you can see the different created Dags 
![image](https://github.com/kadirimeriem/ELT_pipeline_Airflow_Spark_Hbase_ELK/assets/110923887/e9866247-8803-4f6e-a09b-ddf0ecc03901)
![image](https://github.com/kadirimeriem/ELT_pipeline_Airflow_Spark_Hbase_ELK/assets/110923887/ed32cca9-a2e1-4e0d-9b8e-2ebc0418a688)

•	Kibana : http://localhost:5601
Where you can create some visualisations
![image](https://github.com/kadirimeriem/ELT_pipeline_Airflow_Spark_Hbase_ELK/assets/110923887/be37b520-f1c3-4567-bae5-0a0bed6f31a8)
![image](https://github.com/kadirimeriem/ELT_pipeline_Airflow_Spark_Hbase_ELK/assets/110923887/32dd4cdb-8999-4e1f-8fa9-0785d47d1eba)

# Some results

![image](https://github.com/kadirimeriem/ELT_pipeline_Airflow_Spark_Hbase_ELK/assets/110923887/219b9567-2576-41f2-b423-2a4dcfac5ad6)
![image](https://github.com/kadirimeriem/ELT_pipeline_Airflow_Spark_Hbase_ELK/assets/110923887/4581b831-6963-4e28-829f-800c190c71b5)




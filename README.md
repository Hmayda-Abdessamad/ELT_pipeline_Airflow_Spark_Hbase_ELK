# Automated-Big-Data-Visualization-Pipeline-using-Apache-Airflow-and-ELK-Stack
Purpose: The project aims to automate the collection, processing, and visualization of financial data, enabling users to gain insights and make informed decisions based on the analyzed data. By integrating multiple technologies like Apache Airflow, Spark, HBase, Elasticsearch, and Kibana,

# Requirements

To run this project locally, ensure you have the following installed:

1) Docker
2) Python
   
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


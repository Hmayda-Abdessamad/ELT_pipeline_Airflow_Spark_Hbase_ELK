import Utils
import happybase
from elasticsearch import Elasticsearch
from datetime import datetime


if __name__ == "__main__":

    # Create a Spark session
    spark = Utils.create_spark_connection(appName="income_statement_preprocess")
    connection = Utils.create_hbase_connection()
    table=connection.table("income_statement")
    es=Elasticsearch([{"host":"elasticsearch","port":9200,'scheme': "http"}])

    # Iterate through HBase data and index into Elasticsearch
    for key, data in table.scan():
      
        # Assuming 'key' is the timestamp and 'data' contains the financial market information
        decoded_key = key.decode('utf-8')
        decoded_key = datetime.strptime(decoded_key, '%Y-%m-%d')
        decoded_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in data.items()}  # Decode data
        print(f"key : {decoded_key} , data : {decoded_data}")
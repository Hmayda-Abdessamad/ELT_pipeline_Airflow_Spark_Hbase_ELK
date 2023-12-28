
import Utils
import happybase
from elasticsearch import Elasticsearch
from datetime import datetime


if __name__ == "__main__":

    # Create a Spark session
    spark = Utils.create_spark_connection(appName="historical_data_preprocess")
    connection = Utils.create_hbase_connection()
    table=connection.table("historical_data")
    es=Elasticsearch([{"host":"elasticsearch","port":9200,'scheme': "http"}])
  

    # Initialize dictionaries for each column family
    adj_close_dict = {}
    Close_dict={}
    High_dict={}
    Low_dict={}
    Open_dict={}
  
    # Iterate through HBase data and index into Elasticsearch
    for key, data in table.scan():
      
        # Assuming 'key' is the timestamp and 'data' contains the financial market information
        decoded_key = key.decode('utf-8')
        decoded_key = datetime.strptime(decoded_key, '%Y-%m-%d %H:%M:%S')
        decoded_data = {k.decode('utf-8'): v.decode('utf-8') for k, v in data.items()}  # Decode data

        adj_close_dict["date"] = decoded_key.isoformat()
        Close_dict["date"]=decoded_key.isoformat()
        High_dict["date"]=decoded_key.isoformat()
        Low_dict["date"]=decoded_key.isoformat()
        Open_dict["date"]=decoded_key.isoformat()
       
        # Iterate over the row data and organize it into respective dictionaries for the current timestamp
        for col_key, value in decoded_data.items():
            column_family, column_name = col_key.split(':')
            if column_family == 'Adj Close':
                #here it should be float
                adj_close_dict[column_name] = float(value)
            elif column_family=="Close":
                Close_dict[column_name]=float(value)
            elif column_family=='High':
                High_dict[column_name]=float(value)
            elif column_family=="Low":
                Low_dict[column_name]=float(value)
            elif column_family=="Open":
                Open_dict[column_name]=float(value)
            

       
        # Index the document into Elasticsearch
        es.index(index='history_adj_close', document=adj_close_dict)
        es.index(index='history_close', document=Close_dict)
        es.index(index='history_high', document=High_dict)
        es.index(index='history_low', document=Low_dict)
        es.index(index='history_open',document=Open_dict)
        
  

    print("Indexing into Elasticsearch completed")
   
import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, explode
from pyspark.sql.types import  StructField, StringType, ArrayType
import happybase
import threading

# Define a lock
table_creation_lock = threading.Lock()
# first let's create our spark session 
def create_spark_connection():
    s_conn=None
    # create spark conn here
    try:
        s_conn=SparkSession.builder.appName("Historical_data").getOrCreate()
        s_conn.sparkContext.setLogLevel("ERROR")
        logging.info("Spark connection created succesfully")
    except Exception as e:
        logging.error(f"connection to spark failed due to {e} ")

    return s_conn

def create_hbase_connection():
    #create cassandra conn here
   
    try:
        connection = happybase.Connection("hbase")
        return connection
    except Exception as e:
        logging.error(f"could not create cassandra connection due to {e}")
        return None

def create_hbase_table_if_not_exist(connection, table_name, column_families):
    # Acquire the lock
    table_creation_lock.acquire()

    try:
        # Create a table if it does not exist
        tables = connection.tables()
        if table_name.encode() not in tables:
            column_family_dict = {cf: dict() for cf in column_families}
            connection.create_table(table_name, column_family_dict)
            print("historical_data table created")
        else:
            print("historical_data table already exists")
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        # Release the lock
        table_creation_lock.release()



def insert_data(row,table_name,column_family):
    connection=create_hbase_connection()
    # insertion here
    print("inserting data ...")
    # Check if the table and column family exist, create them if not
    create_hbase_table_if_not_exist(connection, table_name, column_family)
    # Open the table
    table = connection.table(table_name)

     # Insert static data into HBase
    for data in row:
        row_key = data['#']
        values = {
            f"{column_family}:Name": data['Name'],
            f"{column_family}:Price": data['Price'],
            f"{column_family}:24H CHANGE": data['24H CHANGE'],
            f"{column_family}:24H VOLUME": data['24H VOLUME'],
            f"{column_family}:Market Cap": data['Market Cap'],
            f"{column_family}:timestamp": data['timestamp'],
            # Add other columns as needed
        }

    table.put(row_key.encode(), values)
    # Close the connection
    connection.close()
    return "insertion done"
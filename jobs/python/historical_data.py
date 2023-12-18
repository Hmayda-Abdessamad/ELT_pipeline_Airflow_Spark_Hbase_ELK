from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, explode
from pyspark.sql.types import StructType, StructField, StringType, ArrayType
import happybase
import Utils
import Yahoo


df=Yahoo.HistoricalData()
print(df.columns)

def write_to_hbase(row,table_name,cf):
    # Create a connection to HBase
    connection = happybase.Connection("hbase")

    # Check if the table and column family exist, create them if not
    Utils.create_hbase_table_if_not_exist(connection, table_name, cf)

    # Open the table
    table = connection.table(table_name)

    # Extract values from the row
    values = {
	f"{cf}:#": row['#'],
        f"{cf}:Name": row['Name'],
        f"{cf}:Price": row['Price'],
	f"{cf}:24H CHANGE": row['24H CHANGE'],
        f"{cf}:24H VOLUME": row['24H VOLUME'],
        f"{cf}:Market Cap": row['Market Cap'],
        f"{cf}:timestamp": row['timestamp'],
        # Add other columns as needed
    }

    # Write data to HBase
    table.put(row['#'].encode(), values)

    # Close the connection
    connection.close()

if __name__ == "__main__":

    # Create a Spark session
    spark = Utils.create_spark_connection()
    connection = Utils.create_hbase_connection()
    column_families = ['Open', 'Close', 'High', 'Low', 'Volume']
    Utils.create_hbase_table_if_not_exist(connection,"historical_data",column_families)
    print("table created")
  
  
            
        


   
  


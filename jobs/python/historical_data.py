from pyspark.sql import SparkSession
import happybase
import Yahoo_data


# Initialize Spark session
spark = SparkSession.builder.appName("Historical_data").getOrCreate()

# get data historical
df=Yahoo_data.HistoricalData()
df=df.reset_index()
df=spark.createDataFrame(df)
#print(df.show())

df.createOrReplaceTempView("historical_data")


shape_df = spark.sql("SELECT * FROM historical_data")


#print(shape_df.show())

# Perform Spark SQL query to select data with ticker column
#result = spark.sql("SELECT *, Ticker FROM stock_data")

# Show the resulting DataFrame
#result.show()




def connect_to_hbase():
    # Define the connection settings
    hbase_host = 'localhost'  # This is the service name from the docker-compose.yml file
    hbase_port = 9090  # Port for HBase
    connection = happybase.Connection(host=hbase_host,port=9090,autoconnect=True)
    def fetch_table():
            return connection.tables()
    fetch_table()
    connection.close()
    

    

# Call the function to execute the HBase operations
connect_to_hbase()



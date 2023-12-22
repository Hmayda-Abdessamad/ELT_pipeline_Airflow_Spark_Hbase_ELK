
import Utils
import Yahoo

#get historical data from yfinance
df=Yahoo.HistoricalData()

column_families=df.columns.levels[0]
# Generating families dictionary using the elements from column_families
column_families_dict = {f'{value}': dict() for i, value in enumerate(column_families)}
# columns_famillies as a list of strings
column_families_str= [str(value) for value in column_families]




if __name__ == "__main__":

    # Create a Spark session
    spark = Utils.create_spark_connection(appName="historical_data")
    connection = Utils.create_hbase_connection()
    Utils.create_hbase_table_if_not_exist(connection,"historical_data",column_families_dict)
    Utils.insert_historical_data(connection,'historical_data')
        
   
  
  
            
        


   
  


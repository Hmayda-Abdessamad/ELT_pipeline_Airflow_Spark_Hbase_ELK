
import Utils
import Yahoo



column_families=Yahoo.get_income_statements_common_columns()


if __name__ == "__main__":

    # Create a Spark session
    spark = Utils.create_spark_connection(appName="income_statement")
    connection = Utils.create_hbase_connection()
    Utils.create_hbase_table_if_not_exist(connection,table_name="income_statement",column_families=column_families)
    Utils.insert_income_statement_data(connection=connection,table_name="income_statement")

        
   
  
  
            
        


   
  


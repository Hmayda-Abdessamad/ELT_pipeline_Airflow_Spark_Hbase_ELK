
import Utils
import Yahoo

#get historical data from yfinance
df=Yahoo.get_shares_full()

column_families=df.columns[1:3]
# Generating families dictionary using the elements from column_families
column_families_dict = {f'{value}': dict() for i, value in enumerate(column_families)}



if __name__ == "__main__":

    # Create a Spark session
    spark = Utils.create_spark_connection(appName="shares_data")
    connection = Utils.create_hbase_connection()
    Utils.create_hbase_table_if_not_exist(connection,"shares_data",column_families=["full_shares"])
    Utils.insert_shares_data(connection,'shares_data')
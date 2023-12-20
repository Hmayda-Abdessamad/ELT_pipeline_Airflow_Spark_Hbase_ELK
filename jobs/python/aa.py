from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, explode
from pyspark.sql.types import StructType, StructField, StringType, ArrayType
import happybase
import Utils
import Yahoo
import Utils


df = Yahoo.HistoricalData()  # Assuming this retrieves some data or initializes DataFrame
column_families = df.columns.levels[1]

# Generating families list using the elements from column_families
families = [str(value) for value in column_families]

print(df.shape)


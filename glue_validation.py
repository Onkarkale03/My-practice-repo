from pyspark.sql.functions import *

df = df.dropDuplicates(["customer_id"])

df = df.filter(col("customer_id").isNotNull())

df = df.withColumn(
    "email",
    lower(trim(col("email")))
)

df = df.withColumn(
    "created_date",
    current_timestamp()
)

df_invalid = df.filter(col("age") < 0)

df_valid = df.filter(col("age") >= 0)
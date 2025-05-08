from pyspark.sql import SparkSession

# the following code is the same as local_code_test_A2-pyspark-sql.py excpet for some modifications
# and the reference are all the same as local_code_test_A2-pyspark-sql.py.

# Start a local Spark session
spark = SparkSession.builder.master("local[*]").appName("PokemonFeistinessSQL").getOrCreate()

# Load the dataset from CSV
pokemon_df = spark.read.csv("hdfs:///user/ubuntu25/yarn/pokemon.csv", header=True, inferSchema=True)



# Register DataFrame as a temporary SQL table
pokemon_df.createOrReplaceTempView("pokemon")

# Step 1: Compute Feistiness and Rank Pokémon
query = """
    WITH FeistinessRank AS (
        SELECT 
            type1,
            COALESCE(type2, 'unknown') AS type2, 
            name,
            ROUND(attack / weight_kg, 2) AS feistiness,
            RANK() OVER (PARTITION BY type1 ORDER BY attack / weight_kg DESC) AS rank
        FROM pokemon
        WHERE weight_kg > 0  -- Avoid division by zero
    )
    SELECT type1, type2, name, feistiness 
    FROM FeistinessRank
    WHERE rank = 1
    ORDER BY type1
"""

# Run the SQL query
feistiest_pokemon = spark.sql(query)

# Show results
feistiest_pokemon.show()

# Save results to CSV
feistiest_pokemon.coalesce(1).write.option("header", "true")\
    .option("delimiter", ",")\
    .mode("overwrite")\
    .csv("hdfs:///user/ubuntu25/yarn/output")



# Stop the Spark session
spark.stop()

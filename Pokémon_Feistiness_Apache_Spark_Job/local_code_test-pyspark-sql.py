from pyspark.sql import SparkSession

# reference for the above[1]. *

# Start a local Spark session
#reference for the following[1],[2]. *
spark = SparkSession.builder.master("local[*]").appName("PokemonFeistinessSQL").getOrCreate()


# Load the dataset from CSV

# reference for how to do the following[3]. *

# reference that explain why to use file or hdfs[4]. *
pokemon_df = spark.read.csv("file:///home/ubuntu25/School_grad/Amod5410/Assignement2/to_upload/pokemon.csv", header=True, inferSchema=True)


# Register DataFrame as a temporary SQL table
# reference for knowing how to this[5]. *
pokemon_df.createOrReplaceTempView("pokemon")

# Step 1: Compute Feistiness and Rank Pokémon 

# references for the following query[6],[7],[8],[9],[10],[11]. * 
# Gemini helped organise the final the code and debug errors.

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
# reference for the following[5]. *
feistiest_pokemon = spark.sql(query)

# Show results
# reference for the following[5]. *
feistiest_pokemon.show()

# Save results to CSV
# reference for how to do the following[12], [13], [14]. *

feistiest_pokemon.coalesce(1).write.option("header", "true")\
    .option("delimiter", ",")\
    .mode("overwrite")\
    .csv("file:///home/ubuntu25/School_grad/Amod5410/Assignement2/to_upload/output")


# Stop the Spark session
# reference for the following[15]. *
spark.stop()

# reference for all the code in the readme file.
# The sections marked with (*) indicate 
# where there is code sourced, 
# referenced, or where the understanding 
# was derived from another source other than myself.

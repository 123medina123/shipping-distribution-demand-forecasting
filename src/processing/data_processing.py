from pyspark.sql import SparkSession

def process_data():
    # Create a SparkSession
    spark = SparkSession.builder.appName('data_processing').getOrCreate()

    # Read the CSV file into a DataFrame
    df = spark.read.csv('data/data.csv', inferSchema=True, header=True)

    # Perform data cleaning operations...
    # For example, let's remove rows with missing values
    df = df.na.drop()

    # Save the cleaned data to a new CSV file
    df.write.csv('data/cleaned_data.csv', header=True)

if __name__ == '__main__':
    process_data()
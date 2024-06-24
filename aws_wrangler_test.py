import os
import awswrangler as wr

# take the cred from env
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# split the cred from env
aws_access_key_id = aws_access_key_id.split(':')[1]
aws_secret_access_key = aws_secret_access_key.split(':')[1]

# Set the AWS credentials and region
os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'  # Replace 'us-east-1' with your region

# Example function to run an Athena query
def run_athena_query(query, database, s3_output):
    try:
        df = wr.athena.read_sql_query(
            sql=query,
            database=database,
            ctas_approach=False,  # Use False to fetch the result directly instead of creating a new table
            s3_output=s3_output
        )
        return df
    except Exception as e:
        print(f"Error running Athena query: {e}")
        return None

# Example usage
query = """SELECT * FROM "default"."s3_salaries" LIMIT 10;"""  # Use triple quotes for multi-line strings
database = "s3_analyze_salaries_db"
s3_output = "s3://athenajenkinstestbucket/"

df = run_athena_query(query, database, s3_output)
if df is not None:
    print("Query executed successfully.")
    print(df)
else:
    print("Query execution failed.")
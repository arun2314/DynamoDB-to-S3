import csv
import json
import boto3
from io import StringIO

# Initialize AWS Clients
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

# Updated Table and Bucket Names
TABLE_NAME = 'UserData'  # Updated DynamoDB Table Name
BUCKET_NAME = 'dynamodb-csv-export-bucket'  # Updated S3 Bucket Name

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)
    
    # Scan DynamoDB Table
    response = table.scan()
    items = response.get('Items', [])

    if not items:
        return {
            'statusCode': 200,
            'body': 'No data found in DynamoDB table'
        }

    try:
        # Create CSV in memory
        csv_buffer = StringIO()
        writer = csv.DictWriter(csv_buffer, fieldnames=items[0].keys())
        writer.writeheader()
        writer.writerows(items)

        # Upload CSV to S3
        s3.put_object(Bucket=BUCKET_NAME, Key='dynamodb_data.csv', Body=csv_buffer.getvalue())

        return {
            'statusCode': 200,
            'body': 'CSV file created and uploaded to S3 successfully!'
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }

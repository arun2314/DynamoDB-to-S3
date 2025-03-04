# DynamoDB-to-S3

Step 1: Set up the S3 bucket
✔ Go to the S3 console and click "Create bucket."
✔ Name the bucket dynamodb-csv-export-bucket (or any unique name).
✔ Leave all settings as default and click "Create bucket."

Step 2: Create the DynamoDB table
✔ Go to the DynamoDB console and click "Create table."
✔ Set the Table name to UserData.
✔ Set the Partition key to id (String).
✔ Add sample data:

{
  "id": "1",
  "name": "Alice",
  "email": "alice@example.com"
}
Step 3: Create the Lambda function
✔ Go to the Lambda console and click "Create function."
✔ Set the Function name to DynamoDBToCSV.
✔ Choose Python 3.12 as the runtime.
✔ Select Create a new role with basic permissions.

Step 4: Add permissions to the Lambda role
✔ Go to IAM → Roles and find your Lambda role.
✔ Attach the following policies:
➡ AmazonDynamoDBReadOnlyAccess
➡ AmazonS3FullAccess

Step 5: Write the Lambda function
✔ Replace the default code with your Lambda function (lambda_func.py).

Step 6: Test the function
✔ In the Lambda console, click "Test" and create a new test event (empty payload).
✔ Click "Test" again and ensure you see a success message.
✔ Go to your S3 bucket and check for the dynamodb_data.csv file.

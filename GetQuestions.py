import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
questionTable = dynamodb.Table("Questions")

def lambda_handler(event, context):
    questions = questionTable.scan()
    
    return {
        'statusCode': 200,
        'body': json.dumps(questions)
    }

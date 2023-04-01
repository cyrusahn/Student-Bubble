import json
import boto3
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table('Questions')
    title = event['title']
    Question = event['Question']
    response = table.put_item(
        Item={
            'title': title,
            'Question' : Question,
            })
    return {
        'statusCode': 200,
        'body': json.dumps('Question posted!')
    }
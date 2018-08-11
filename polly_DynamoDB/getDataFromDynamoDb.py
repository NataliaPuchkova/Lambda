import os
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    
    postId = '*'  #event["id"]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Clients')
    
    if postId=="*":
        items = table.scan()
    else:
        items = table.query(
            KeyConditionExpression=Key('email').eq(postId)
        )
    return items["Items"]

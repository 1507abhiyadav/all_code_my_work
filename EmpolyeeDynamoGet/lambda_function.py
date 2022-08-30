import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employee')
def lambda_handler(event, context):
    # print(event)
    # data = 
    # dynamodb = boto3.resource('dynamodb')
    # table = dynamodb.Table('employee')
    # response=table.get_item(
    #     Key={
    #         "id":3
            
    #     },
    #     )  # data stored as  dict  formate
    # data = event["queryStringParameters"]["id"]
    
    # resource = table.get_item(Key = {"id":data})
    # print(response["Item"])
    # return response["Item"]
    response = table.scan()
    print(response)
    return {
        'statusCode': 200,
        'body': response['Items']
      }
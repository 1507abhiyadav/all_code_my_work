import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employee')

def lambda_handler(event, context):
    # dynamodb = boto3.resource('dynamodb')
    # table = dynamodb.Table('employee')
    print(event)
    if len(event)==0:
        return {
            "statusCode":200,
            "message": "event(payload) is required"
        }
    # response = table.put_item(
    # Item={
    #     'id': 6,
    #     'name': 'raka',
    #     'salary': 40000
    #     # 'age': 40
    # },
    # )
    # return response
    body = table.scan()
    # print(body)
    # print(type(body))
    # print(body["Items"])
    data = body["Items"]
    var = False
    for i in range(len(data)):
      if data[i]['id'] == event['id']:
        var= True
        return {
            "statusCode":200,
            "message":"Id already exists"
            }
    else:
        response = table.put_item(Item=event)
        return("Data successfully add")
    
    
    # response = table.put_item(Item=event)
    # return("Data successfully add")
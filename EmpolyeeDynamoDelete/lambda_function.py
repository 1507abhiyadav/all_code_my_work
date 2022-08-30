import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('employee')
    # response = table.delete_item(
    #     Key={
    #         "id":2
    #     },
    # )
    if len(event) == 0:
        return {
            "statusCode" : 400,
            "message"  :"event(payload) is required"
            
        }
    # print(event)
    # return {
    #     "statusCode":200,
    #     "body":"hello "
    # }
    body = table.scan()
    # print(body)
    # print(type(body))
    # print(body["Items"])
    data = body["Items"]
    # print(data)
    var = False
    if len(data)==0:
        return {
            "statusCode":200,
            "data":"empty"
        }
    for i in range(len(data)):
        if data[i]["id"] == event["id"]:
            var = True
            # print()
            # data.pop(i)
            table.delete_item(
                Key={
                  "id":event["id"]
                },
            )
            return {
                "statusCode":200,
                "message":"Data successfully delete",
            }
    # print("Id not found")
    return {
            "statusCode":200,
            "message": "Id not found"
        }
        
        
        
        
## ###########    Delete Table    #####################


# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('employee')
# table.delete()

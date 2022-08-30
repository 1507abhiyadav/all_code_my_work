## data converted into sting
import json
## dynamodb import
import boto3  

### lambda function  where tow parameter one event is required and second is optional
def lambda_handler(event, context):  
    print(event)
    ##  resource of dynamodb 
    dynamodb = boto3.resource('dynamodb')
    ## table name 
    table = dynamodb.Table('employee') 
    if len(event)==0:  ## payload is not exists
      return{
            "statusCode" : 400,
            "message"  :"event(payload) is required"
      }
    ### read all data in table
    body = table.scan()  
    # print(body)
    # print(type(body))
    # print(body["Items"])
    ## Items as dict keys  ----- gives actual data
    data1 = body["Items"]  
    # print(data)
    var = False
    for i in range(len(data1)):
        #### I compare to stored data and  coming data(payload) 
        if data1[i]["id"] == event["id"]: 
            var = True
            # print(data)
            # data[i] = event
            ## data update--- there are so many parameter of update_item method to update date 
            response = table.put_item(Item=event)
            return("Data successfully update")
            # response = table.update_item(
            #      ### Key is required to update data
            #     Key={'id': event["id"]}, 
            #     UpdateExpression='SET event=:D',  # update expression  SET'

            #     ExpressionAttributeNames={  # attributes value
            #         ':D': data1
            #     },
            #     # # ExpressionAttributeNames= {
                # #      '#U': 'data[i]''
                # # },
                # #####  update expression  SET
                # # UpdateExpression ='SET data1  = :u',
                #  #####   attributes name present in table. which i want to update
                # ExpressionAttributeNames = {     
                   
                #     '#U': 'name',
                #     '#A': 'age'
                # #     ':u': 'event'
                #  },
                # ###### attributes value
                # ExpressionAttributeValues = {   
                #     # ':u': event,
                #     ':u':event["name"],
                #     ':a':event["age"]
                # },
                # UpdateExpression ='SET #U = :u, A = :a',
                # # ConditionalOperator ,
                # ConditionalOperator : "#U OR #A",
                # # ReturnValues = "UPDATED_NEW"
                # ReturnValues = "ALL_NEW",
                # ReturnValues = "ALL_OLD"
            # )
    # #         # print(data)
            # return {
            #     "statusCode":200,
            #     "message":"Data successfully update",
            #     "data":response['Attributes'],
            # }
    # # print("Id not found")
    return {
            "statusCode":200,
            # "body": json.dumps("Id not found")
            "message":"Id not found"
        }

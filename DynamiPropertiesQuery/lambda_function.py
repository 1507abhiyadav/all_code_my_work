import json
import boto3
payload=[
        "id":1,
        "name":"abhishek",
        "age":23
    ]
    
def lambda_handler(event, context):
    # payload={
    #     "id":1,
    #     "name":"abhishek",
    #     "age":23,
    #     "phone":"aaaaaaaaa"
    # }
    # dynamodb = boto3.resource('dynamodb')
    # table = dynamodb.Table('employee')
    response = payload.update_item(
        Key ={
             "id":payload["id"]
        },
        ExpressionAttributeNames = {
            '#U': 'name',
            '#A': 'age'
        },
        ExpressionAttributeValues = {
            ':u':"Abhishek Yadav",
            ':a':24
        },
        UpdateExpression ='SET #U= :u,#A = :a',
        # ConditionExpression= "#U =:u AND #A =:a",
        # ReturnValues = "UPDATED_NEW"
        ReturnValues = "ALL_NEW",
        # ReturnValues = "ALL_OLD"
        )
    return response['Attributes']
    
    # # print(type(payload))
    # keys = list(payload.keys())
    # # print(keys)
    # values = list(payload.values())
    # # print(values)
    # resp = table.update_item(
    #     Key={'id': 1},
    #     # UpdateExpression="SET #" + keys[2] + "=:a",
    #     # ExpressionAttributeNames = { "#"+keys[2]: keys[2]},
    #     # ExpressionAttributeValues={':a' : values[2]},
    #     # UpdateExpression="SET #age =:n",
    #     # ExpressionAttributeNames= {'#age':'age'},
    #     # ExpressionAttributeValues={':n':26},
    #     UpdateExpression="SET age = :s","SET name = :n" 
    #     ExpressionAttributeValues={':s':34567,
    #     "msd": ':n'},
    #     ReturnValues="ALL_NEW",
    #     )
    # # UpdateExpression="SET keys[2]= :s ,keys[1] = :n",
    # # ExpressionAttributeValues={':s': values[2], ':n' :values[1]},
    # ## ReturnValues="UPDATED_NEW",
    # # UpdateExpression='SET age = :val1, value2 = :val2',
    # # ExpressionAttributeValues={
    # #  ':val1': someValue1,
    # #  ':val2': someValue2
    # # }
    # #             )
    # print(resp['Attributes'])
    # # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': resp['Attributes']
    # }


# response = table.update_item(
    #     Key={'id': event["id"]},
    #     ExpressionAttributeNames = {
    #         '#U': 'name',
    #         '#A': 'age'
    #     },
    #     ExpressionAttributeValues = {
    #         ':u':event["name"],
    #         ':a':event["age"]
    #     },
    #     UpdateExpression ='SET #U= :u,#A = :a',
    #     # ConditionExpression= "#U =:u AND #A =:a",
    #     # ReturnValues = "UPDATED_NEW"
    #     ReturnValues = "ALL_NEW",
    #     # ReturnValues = "ALL_OLD"
    # )
    # return response['Attributes']
    
    
    #  UpdateExpression="set #colName= :st, user_name= :usr",
    #     ExpressionAttributeValues={
    #         ':st' : event['source/target'],
    #         ':usr' : event['user_name']
    #             },
    #     ExpressionAttributeNames={
    #         '#colName' : 'source/target'
    #             },
    #     ReturnValues="UPDATED_NEW"
    # ) 
    #     UpdateExpression="SET #name =:n",
    #     ExpressionAttributeNames= {'#name':'name'},
    #     ExpressionAttributeValues={':n':"abhishek Yadav"},
    #     # UpdateExpression="SET salary= :s",
    #     # ExpressionAttributeValues={':s': 60000},
    #     # ReturnValues="UPDATED_NEW",
    #     # ReturnValues="UPDATED_OLD"
    #     ReturnValues="ALL_NEW"
    # )
    # print(response['Attributes'])
    # return response['Attributes']
    # TODO implemen
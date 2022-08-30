import json
employee =[{
  "id":1,
  "name":"abhishek"
},
{ "id":2,
  "name":"rakesh"
},
{
  "id":3,
  "name":"abhi"
},
{ "id":4,
  "name":"raka"
},
{ "id":5,
  "name":"sandeep"
}]

def lambda_handler(event, context):
    print(event)
    # print(event['body'])
    if len(event)==0:
      return{
            "statusCode" : 400,
            "message"  :"event(payload) is required"
      }
    # print(type(event['body']))
    # data= event['body']
    # data = json.loads(event['body'])
    var = False
    for i in range(len(employee)):
        if employee[i]["id"] == event["id"]:
            var = True
            print(employee)
            employee[i] = event
            print(employee)
            return {
                "statusCode":200,
                # "body": json.dumps(employee)
                "message":"Data successfully update",
                "employee": employee
            }
    # print("Id not found")
    return {
            "statusCode":200,
            # "body": json.dumps("Id not found")
            "message":"Id not found"
        }
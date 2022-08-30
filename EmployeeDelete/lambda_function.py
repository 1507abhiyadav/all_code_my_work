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
    var = False
    if len(employee)==0:
        return {"[]"}
    for i in range(len(employee)):
        if employee[i]["id"] == event["id"]:
            var = True
            # print(employee)
            employee.pop(i)
            # print(employee)
            return {
                "statusCode":200,
                "message":"Data successfully delete",
                "employee":employee
            }
    # print("Id not found")
    return {
            "statusCode":200,
            "message": "Id not found"
        }
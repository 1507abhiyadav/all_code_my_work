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
    # print(employee)
    # print(json.dumps(employee))
    return {
        'status': 200,
        "message":"Data successfully get",
        # 'body': json.dumps(employee) ## print as likes {\"id\": 1, \"name\": \"abhishek\"}
        'employee': employee
    }
 
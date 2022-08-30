import json
employee = []
def lambda_handler(event, context):
    print(event)
    if len(event)==0:
      return{
            "statusCode" : 400,
            "message"  :"event(payload) is required"
      }
    # print('event start')
    # print(type(event))
    # print(event)
    # print('event end')
    # return event
    # employee.append(event)
    # return employee
    var = False
    for i in range(len(employee)):
      if employee[i]['id'] == event['id']:
        var= True
        return {
            "statusCode":200,
            "message":"Id already exists"
            }
    else:
        employee.append(event)
        return {
            "statusCode":200,
            "message":"Data successfully add",
            "employee":employee
        }

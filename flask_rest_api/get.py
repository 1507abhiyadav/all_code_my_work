from ast import arg
from dataclasses import field, fields
from email import message
import this
from flask import Flask
import flask
from flask_restful import Resource,Api, marshal_with,reqparse,abort
from pkg_resources import require
from requests import delete
from flask_mongoengine import MongoEngine
app = Flask(__name__)
api = Api(app)
app.config['MONGODB_SETTING']={
    'db':'todomodel',
    'host':'localhost',
    'port':27017
}
db=MongoEngine()
db.init_app(app)


# class helloworld(Resource):
#     def get(self):
#         return {'name':'Abhishek Yadav'}

# class helloName(Resource):
#     def get(Self,Name):
# 
#         return {'team': 'hello, My name is  {}'.format(Name)}
class Todomodel(db.Document):
    _id=db.IntField()
    task= db.StringField()
    summary=db.StringField()

todos = {
    1:{"task":"task1","summary":"this is first id task"},
    2:{"task":"task2","summary":"this is second id task"},
    3:{"task":"task3","summary":"this is third id task"},
}

resoure_field={
    "_id":fields.Integer,
    "task":fields.String,
    "summary":fields.String
}
### add data in todos
task_post_args= reqparse.RequestParser()
task_post_args.add_argument("task",type=str,help="this is required",required=True)
task_post_args.add_argument("summary",type=str,help="this is required",required=True )
### update data in todos
task_update_args=reqparse.RequestParser()
task_update_args.add_argument('task',type=str)
task_update_args.add_argument('summary',type=str)
class ToDo(Resource):
    @marshal_with(resoure_field)
    def get(self,todo_id):
        obj = Todomodel.objects.get(_id=todo_id)
        if not obj:
            abort(400,message="id not found")
        return obj
        # return todos[todo_id]
    @marshal_with(resoure_field)
    def post(self,todo_id):
       
        args= task_post_args.parse_args()
        # if todo_id in todos: 
        #     abort(401,message ='task Id already exists')
        # todos[todo_id] = {"task":args["task"],"summary":args["summary"]}
        # return todos
        todo = Todomodel(_id=todo_id,task=args['task'],summary=args['summary']).save()

        return todo,200
    @marshal_with(resoure_field)
    def put(self,todo_id):
        args = task_update_args.parse_args()
        if todo_id not in todos:
            abort(401,message= "id does not exists")

        # if args['task']:
        #     todos[todo_id]['task']= args['task']
        # if args['summary']:
        #     todos[todo_id]['summary']=args['summary']
        # return todos
        if args['task']:
            Todomodel.objects.get(_id=todo_id).update(task=args['task'])

        if args['summary']:
            Todomodel.objects.get(_id=todo_id).update(summary=args['summary'])
        return "{} updated".format(todo_id),200
    @marshal_with(resoure_field)
    def delete(self,todo_id):
        if todo_id not in todos:
            abort(401,message= "id does not exists")
        Todomodel.objects.get(_id=todo_id).delete()
        return "deleted",200

class Todo_set(Resource):
    def get(self):
        return todos
api.add_resource(ToDo,'/todos/<int:todo_id>')
api.add_resource(Todo_set,'/todos')
# api.add_resource(helloworld,'/helloworld')
# # get localhost:5000/helloworld
# #    helloworld
# api.add_resource(helloName,'/helloworld/<string:Name>')
# #get localhost:5000/helloworld/Hero
#     hello Hero

if __name__ == '__main__':
    app.run(debug=True)





##### using route mothed
# 
#     
# from flask import Flask
# app = Flask(__name__)

# @app.route('/flask')
# def hello_flask():
#    return 'Hello Flask'

# @app.route('/python/')
# def hello_python():
#    return 'Hello Python'

# @app.route('/flask/details')
# def hello_flask1():
#     return 'flask is a web application framework. it was developed by Armin Ronacher '

# if __name__ == '__main__':
#    app.run()

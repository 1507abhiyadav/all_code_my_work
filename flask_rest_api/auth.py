from distutils.log import debug
from venv import create
from flask  import Blueprint

auth = Blueprint("auth",__name__,url_prefix="/api")

@auth.post('/register')
def register():
    return "user created"

@auth.get('/me')
def me():
    return {'user':'me'}

if __name__ =="__main__":
    auth.run(debug=True)
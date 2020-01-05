
from flask import Flask
app = Flask(__name__) 
print(__name__) #this prints __main__

@app.route('/')
def hello_world():
    return 'Hello, World!'



from flask import Flask
app = Flask(__name__) 

#print(__name__) #this prints __main__

@app.route('/')
def hello_world():
    return 'Hello, Keerthana!, you aree on a road to become a software engineer! ultimate vision for 2020'

@app.route('/blog')
def blog():
    return 'I have create a blog'


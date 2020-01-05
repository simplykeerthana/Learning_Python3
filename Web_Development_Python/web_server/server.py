
from flask import Flask, render_template
app = Flask(__name__) 

#render_template allows you to send html files.
#print(__name__) #this prints __main__

@app.route('/')
def hello_world():
    return 'Hello, Keerthana!, you aree on a road to become a software engineer! ultimate vision for 2020'

@app.route('/blog')
def blog():
    return 'I have create a blog'

@app.route('/blog/2020/dogs')
def blog2():
    return 'this is my dogs'

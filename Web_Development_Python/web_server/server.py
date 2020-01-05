import os


from flask import Flask, render_template, send_from_directory
app = Flask(__name__)
 

#render_template allows you to send html files.
#print(__name__) #this prints __main__

@app.route('/')
def hello_world():
    print( url_for('static', filename='bolt.ico'))
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

#@app.route('/favicon.ico') #to show icon
#def favicon():
  #  return send_from_directory(os.path.join(app.root_path, 'static'),
                            #'favicon.ico', mimetype='image/System-software-update.svg.png')


@app.route('/blog')
def blog():
    return 'I have create a blog'

@app.route('/blog/2020/dogs')
def blog2():
    return 'this is my dogs'

#for css and java script  you need a static folder
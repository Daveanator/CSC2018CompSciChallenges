from flask import Flask  #imports the Flask module functionality and creating a Flask Webserver
app = Flask(__name__)  #represents this current file, whatever you named it, will act as your web application

@app.route('/') #this represents the default page, the below function is what is displayed
def hello_world():
    return '<h1>Hello, World!</h1><p>You got your server running! :D</p><p>This is some HTML that is being displayed</p>'
#just some HTML text to demonstrate that the server is working
if __name__ == '__main__': #this is the name assigned to the programme when it is ran
    app.run(debug = True) #this allows us to track errors and make changes to the code without having to restart the server

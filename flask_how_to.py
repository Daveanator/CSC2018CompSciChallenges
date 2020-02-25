1. from flask import Flask  #imports the Flask module functionality and creating a Flask Webserver
2. app = Flask(__name__)  #represents this current file, whatever you named it, will act as your web application
3.
4. @app.route('/') #this represents the default page, the below function is what is displayed
5. def hello_world():
6.    return '<h1>Hello, World!</h1><p>You got your server running! :D</p><p>This is some HTML that is being displayed</p>'
7. #just some HTML text to demonstrate that the server is working
8. if __name__ == '__main__': #this is the name assigned to the programme when it is ran
9.     app.run(debug = True) #this allows us to track errors and make changes to the code without having to restart the server

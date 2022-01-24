import os
from flask import Flask
if os.path.exists("env.py"):
    import env

# Create instance of Flask
app = Flask(__name__)


# To make sure the app is properly configured
# this defauls to the default route
@app.route("/")  
def hello():
    return "Hello World ... again!"


#  Tell the app how and when to run the application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) 
            # change debug to False before project deployment/submission

            
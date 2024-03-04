from os import name
from flask import Flask


app = Flask(__name__)

@app.route("/")
def Hello_word():
    return " Hello Word!"

if __name__ == "__main__" :
 app.run(debug=True, host="localhost",   port=5000)    
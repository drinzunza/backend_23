"""
  Desc: Backend for the online store
Author: Sergio Inzunza
"""

from flask import Flask
from test1 import about_me

app = Flask(__name__)


@app.route("/")
def home():
    return "Hi There!!"

@app.route("/about")
def about():
    return f"{about_me['name']} {about_me['last']}"


# TODO: remove debug before deploying
app.run(debug=True)
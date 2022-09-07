from datetime import datetime
from flask import Flask, render_template
from . import app
import requests 
from bs4 import


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    url = "https://raw.githubusercontent.com/fakemail1865/new_rep/main/FinalTest%20%5B0.1%5D.xml"

    with requests.get(url) as rq:
        payload = rq.content

    headers = {
      'Content-Type': 'application/octet-stream',
      'Authorization': 'Basic c2VtYWRtaW46c2VtYWRtaW4=',
      'Cookie': 'XSRF-TOKEN=a3dc895f-3443-4952-8d6e-a492d2218e14'
    }

    #send post request to semarchy
    name = "testnew"  # name of model you want to import
    key = 0.0 
    url = "http://20.24.242.37/semarchy/api/rest/app-builder/models/{name}/editions/{key}/content".format(name=name,key=key)

    response = requests.request("POST", url,  headers=headers, data=payload)

    
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

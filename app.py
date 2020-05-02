from flask import Flask, render_template, request
import os
from jinja2 import Template

app=Flask("Application")


@app.route("/")
def index():
  return render_template("welcome.html")

def bank(x):
    global var
    if x==1:
        var="banker"
    elif x==2:
        var="player"
    else :
        var="banpla"
    return 

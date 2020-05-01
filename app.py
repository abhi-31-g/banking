from flask import Flask, render_template, request
import os

app=Flask("Application")

@app.route("/")
def index():
    return render_template("welcome.html")

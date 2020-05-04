from flask import Flask, render_template, request
import os
from jinja2 import Template
import sqlalchemy as sql
import random
import string
from sqlalchemy.orm import scoped_session, sessionmaker

app=Flask("Application")
engine=sql.create_engine('postgresql://postgres:veronica31@localhost:5432/bank')
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
  return render_template("welcome.html")

@app.route("/banker?=login/",methods=["POST"])
def createtable():
  username=request.form.get("Username")
  players=int(request.form.get("players"))
  password="#"+str(random.randint(1000,9999))+"$"
  sessioncode=''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
  try:
    db.execute("create table :scode ( id PRIMARY KEY SERIAL NOT NULL, Name VARCHAR NOT NULL, Balance NUMERIC, Liabilities NUMERIC, Assets VARCHAR);",{"scode": sessioncode})
    db.commit
  except:
    createtable()
  return render_template("banker.html",sesscode=sessioncode,passw=password)
  
  
  
  

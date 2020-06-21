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

@app.route("/banker/login/",methods=["POST"])
def createtable():
  username=request.form.get("Username")
  password=str(random.randint(10000,99999))
  sessioncode=''.join(random.choices(string.ascii_uppercase, k = 8))
  passwi='#'+password+'$'
  try:
    db.execute("create table "+ sessioncode +" ( id SERIAL PRIMARY KEY NOT NULL, Name VARCHAR NOT NULL, Balance NUMERIC, Liabilities NUMERIC, Assets VARCHAR);")
    db.commit()
    db.execute("insert into sessionslog (sesscode, password) values (:scode,:passwi);",{'scode': sessioncode,'passwi': passwi})
    db.commit()
  except:
    createtable()
  db.close()
  return render_template("banker.html",sesscode=sessioncode,passw=password)

@app.route("/player/login/",methods=["POST"])
def login():
  scode=str(request.form.get("scode"))
  passwin=str(request.form.get("passwd"))
  scode.upper()
  passwin.strip('')
  passwic="#"+passwin+"$"
  if db.execute("select * from sessionslog where sesscode= :scode and password= :passwic ;",{"scode": scode,"passwic": passwic}).rowcount==1:
    meinname=str(request.form.get("meinname"))
    db.execute("insert into "+scode+" (Name,Balance) values(:meinname,0)",{'meinname': meinname})
    db.commit()
    return "WELCOME TO THE SESSION"
  else:
    return "UNKNOWN ERROR"

@app.route("/<scode>",methods=["POST","GET"])
def bankpage(scode):
    data=db.execute("select * from "+ scode).fetchall()
    return render_template("bankerspage.html",sesscode=scode,data=data)

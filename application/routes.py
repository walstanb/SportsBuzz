from application import app,db
from flask import render_template, flash, redirect, request
from application.forms import *
from application.models import *
from datetime import date


@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template("index.html")



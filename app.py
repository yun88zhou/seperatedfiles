from flask import Flask

from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__)





@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pet")
def pet():
    return render_template("pet.html")

@app.route("/miao")
def miao():
    return render_template("Miaomiao.html")

@app.route("/qiqi")
def qiqi():
    return render_template("qiqi.html")


@app.route("/enter_result",methods = ['POST'])
def enter_result():
    petname = request.form['pet']
    print(petname)
    if(petname=='qiqi'):
       return render_template("qiqi.html")
    elif(petname=='Miaomiao'):
        return render_template("Miaomiao.html")
    else:
        return render_template("home.html")
    
    
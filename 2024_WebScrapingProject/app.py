from flask import Flask, render_template, request, redirect, url_for
from web_scraper import FindItemByDate, FindSongByName


app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/",methods = ['POST'])
def submit():
    if request.method == "POST":
        user = request.form["nm"]
        return render_template("index.html",output=FindSongByName(user))
    else:
        return render_template("index.html",output="<div style='text-align:center'>NOT FOUND</div>")


if __name__ == "__main__":
    app.run()
import os
import sys

from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
application = app
j = open(r'./static/map/test_map.geojson', "r", encoding="utf8").read()

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")


@app.route('/analytics')
def analytics():
    return render_template("analytics.html")
    

@app.route('/recommendations')
def recomendations():
    return render_template("recommendations.html")

@app.route('/data')
def data():
    return j

if __name__ == '__main__':
    app.run()
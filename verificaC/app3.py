from flask import Flask, render_template, request,redirect,url_for,Response
app = Flask(__name__)


import io
# collegamento al database
import pandas as pd
import pymssql

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

matplotlib.use('Agg')
conn = pymssql.connect(server ='213.140.22.237\SQLEXPRESS',user='ghebrous.davide',password='xxx123##',database='ghebrous.davide')

@app.route('/', methods = ['GET'])
def search():
    return render_template("home3.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
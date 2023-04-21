from flask import Flask, render_template, jsonify, send_from_directory, abort, send_file
import os
from controllers.DataController import DataController
from markupsafe import escape
from config import config
from model.NewsInputData import NewsInputData

app = Flask(__name__)
dataCtrl = DataController("Stock-Indicator-News")

@app.get("/")
def home():
    return render_template('views/home.html')

@app.get("/showdata")
def showdata():
    datalist = dataCtrl.list_all_raw_dataset()
    prepdata = dataCtrl.list_all_prep_dataset()
    return render_template('views/datalist.html',datalist = datalist, prepdata = prepdata)

@app.get("/ship/<filename>")
def shipdata(filename):
    file = dataCtrl.compress_prepData_target(filename,"zip")
    dataCtrl.ship_compressed(file)
    return filename

@app.get('/download')
def downloadFile ():
    print("Download file")
    try:
        return send_from_directory(config['static_local'],"hello.txt",as_attachment = True)
    except:
        abort(404)

@app.post('/labelnews')
def label_news():
    return 1



if __name__ == '__main__':
    NewsInputData.test()
    app.run(debug=True,port=5050)

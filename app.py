from flask import Flask,render_template,url_for,Response,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import sqlite3
import os
import random

app=Flask(__name__)
APP_ROUTE = os.path.dirname(__file__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
# db=SQLAlchemy(app)
# Base = automap_base()
# Base.prepare(db.engine, reflect=True)
# Product = Base.classes.trytbl_info

@app.route("/") 
def s():
    return render_template('s.html')

@app.route("/trends", methods = ['GET', 'POST'])
def trends():
    images = ['2020101520h33m09s.jpg', '2020102121h36m49s.jpg', '2020101921h11m44s.jpg', '2020101818h32m08s.jpg', '2020101900h38m57s.jpg', '2020101418h46m07s.jpg', '2020101417h08m06s.jpg', '2020093017h16m02s.jpg', '2020102919h20m52s.jpg', '2020100117h12m02s.jpg', '2020102903h39m07s.jpg', '2020101617h06m27s.jpg', '2020102818h38m52s.jpg', '2020100200h00m49s.jpg', '2020100816h5039s.jpg', '2020101316h10m48s.jpg', '2020100114h43m03s.jpg', '2020101816h09m28s.jpg', '2020101718h32m07s.jpg', '2020101118h38m53s.jpg']
    images = images[:12]
    if request.method == 'POST':
        conn = sqlite3.connect('myntra.db')
        c = conn.cursor()
        # images = []

        att_id = []
        filter_att = request.form.getlist('typeof')
        for query in filter_att:
            for row in conn.execute(f"SELECT id FROM attributes WHERE {query} = 1"):
                att_id.append(row[0])

        color_id = []
        filter_color = request.form.getlist('colourval')
        print(filter_color)
        for query in filter_color:
            # print(f"SELECT id FROM colors WHERE {query} = 1")
            for row in conn.execute(f"SELECT id FROM colors WHERE {query} = 1"):
                color_id.append(row[0])

        lst3 = []
        if len(color_id) == 0:
            lst3 = att_id

        elif len(att_id) == 0:
            lst3 = color_id
        
        else:
            # print(len(att_id), len(color_id))
            lst3 = [value for value in att_id if value in color_id]
            # print(len(lst3))

        images = lst3  
        print(images)
  
        conn.close()
    
    print(images)
    #Remove duplicates
    images = list(set(images))[:12]
    print(images)
    return render_template("trends.html", images = images)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/trial")
def trial():
    conn = sqlite3.connect('myntra.db')
    c = conn.cursor()

    image_list = [row[0] + ".jpg" for row in c.execute("SELECT id, midi FROM attributes WHERE mini_length = 1 AND id <= 4")][:12]
    print(image_list)
    return render_template("trial.html",image_list = image_list)

if __name__=='__main__':
    app.run()

#set FLASK_APP=app.py
#python -m flask run
#http://127.0.0.1:5000/ 
#http://127.0.0.1:5000/trends
#http://127.0.0.1:5000/foryou
#http://127.0.0.1:5000/about
#http://127.0.0.1:5000/trial
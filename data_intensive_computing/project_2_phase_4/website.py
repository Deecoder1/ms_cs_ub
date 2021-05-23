from flask import Flask, redirect, url_for, render_template,request
app = Flask(__name__)


import csv

import json

with open('data.txt') as json_file:
    data = json.load(json_file)

authlist = []
for i in data:
    authlist.append(i)

print(len(authlist))


@app.route("/")
def home():
    return render_template("index.html", colours = authlist)


@app.route('/operation_result/', methods=['POST'])
def operation_result(): 
    author = (request.form['colours'])
    print(data[author])
    co_author_list, num_of_collobs = [],[]
    for i in data[author]:
        co_author_list.append(i+"  :  "+ str(data[author][i]))
    print(co_author_list)
    
    
    return render_template("prediction.html", author = author, registrations = co_author_list)


 

if __name__== "__main__":
    app.run()
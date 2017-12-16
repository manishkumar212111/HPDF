#from __future__ import print_function
from flask import Flask,request,render_template,redirect

import sys

app= Flask(__name__)

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/AAA' , methods=['POST','GET'])
def AAA():
    if request.method == ' POST':
        name=request.form['name']
        file=sys.stdout
        #print name
        print(name,file)

    return "printed on console screen"



app.run(debug=True)



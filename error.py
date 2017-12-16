from flask import render_template,Flask, app

app=Flask(__name__)
@app.route('/robot.txt/')
def error():

    return render_template('error.html')

app.run()
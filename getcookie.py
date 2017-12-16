from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('NAME')
    age = request.cookies.get('AGE')
    if name == '' or name is None:
        return 'cookie Not found'

    return '<h1>welcome ' + name +'  age:' + age+ '</h1>'

app.run(debug=True)

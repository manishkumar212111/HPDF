from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('cookie.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        ck= name+'@'+age
        resp = make_response('setting cookie ----cookie set')
        resp.set_cookie('NAME', name)
        resp.set_cookie('AGE', age)
        return resp
    return "error"
    #return '<h1>Cookie set as Name' + name + ',Age :' + age


'''@app.route('/getcookie')
def getcookie():
    name = request.cookies['NAME']
    #age = request.cookies('AGE')
    return '<h1>welcome '+name+'</h1>'

'''

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return 'Hello world Manish'


app.run(debug=True)

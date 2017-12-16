from flask import Flask,jsonify,render_template
import urllib, json
import requests

app = Flask(__name__)


@app.route('/author')
def author():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    a=[]
    r=requests.get('https://jsonplaceholder.typicode.com/users')
    for i in range(len(data)):
        for keys, values in data[i].items():
            a.append(data[i]['username'])
            print data[i]['username']
            break
    #print data[3]



    return render_template('author.html', a=a,len=len(a))

#author()
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask,jsonify,render_template
import urllib, json
import requests

app = Flask(__name__)


@app.route('/post')
def post():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    a=[]
    b=[]
    r=requests.get('https://jsonplaceholder.typicode.com/posts')
    for i in range(len(data)):
        for keys, values in data[i].items():
            a.append(data[i]['userId'])
            b.append(data[i]['title'])
            #print data[i]['username']
            break
    #print data[3]



    return render_template('post.html', a=a,len=len(a),b=b)

#author()
if __name__ == '__main__':
    app.run(debug=True)

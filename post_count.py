from flask import Flask,jsonify,render_template
import urllib, json
import requests
import numpy as np
app = Flask(__name__)


@app.route('/post_count')
def post_count():
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




    return render_template('post_count.html',a=np.unique(a, return_counts=True), len=len(np.unique(a, return_counts=True)[0]))

#author()
if __name__ == '__main__':
    app.run(debug=True)

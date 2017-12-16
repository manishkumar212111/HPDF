from flask import Flask,request,send_file,render_template
app=Flask(__name__)
@app.route('/image')
def image():
    filename = 'E:\python\Internship\Week1\passport.jpg'
    return send_file(filename, mimetype='image/gif')


@app.route('/html')
def html():
    filename='E:\python\Internship\Week1\templates\post_count.html'
    return render_template('html.html')

app.run(debug=True)
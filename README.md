Let me first introduce myself, My name is Manish Kumar 3rd year student of B.Tech(CS) from Jaipur National University .
Technolgy Used
          
          Language used: Python
          Framework: Python-flask
          IDE: Pycharm Community Edition 2016.3
INSTALLATION
            
      First of all install flask by command - pip install flask
      And then install virtual environment and activate env using command.
       install virtualenv:-pip install virtualenv
       activate it:-venv/bin/activate


Ques 1- A simple hello-world at http://localhost:8080/ that displays a simple string like "Hello World - Arpit"; replace "Arpit" with your own first name).

        Solution:-
         import class Flask from package flask
         define app route 
         and define function hello() and return hello world as response
         finally  app.run() to run program
         check output at http://127.0.0.1:5000/
        Solution File:- HelloWorld.py in folder week1
       
Ques 2- Add a route, for e.g. http://localhost:8080/authors, which:
 a)fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users
 b)fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts
 c)Respond with only a list of authors and the count of their posts (a newline for each author).
Sol:-
                     
        a)Solution File: author.py and author.html
        
        make a folder named templates and within templates all the html file shold be placed so that they can be rendered using render template.
        Class to be imported: Flask,jsonify,render_template,urllib,json
        
        Check output at:-http://127.0.0.1:5000/author after running the program
    
       b)  Solution file: post.py, post.html
        Class to be imported: Flask,jsonify,render_template,urllib,json,requests
        Check output at:-http://127.0.0.1:5000/post after running the program
        
     c)  Solution File:- post_count.py and post_count.html
        check output at:- http://127.0.0.1:5000/post_count
           
  Ques 3- Set a simple cookie (if it has not already been set) at http://localhost:8080/setcookie with the following values: name=<your-first-name> and age=<your-age>.
         
    Sol:- 
               Solution file :- setcookie.py and cookie.html
            In this problem user have to enter name and age in respected textarea in form and then submit and as response cookie will be set.
             check output at:- http://127.0.0.1:5000/
            
  Ques 4-Fetch the set cookie with http://localhost:8080/getcookies and display the stored key-values in it.
        
    Sol:-
             Solution file :- getcookie.py 
           In this problem user can check stored cookie in their browser.
            Check output at:-  http://127.0.0.1:5000/
          
   Ques 5. Deny requests to your http://localhost:8080/robots.txt page. (or you can use the response at http://httpbin.org/deny if needed)
   
    Sol:- 
         Solution at- error.py and error.html
        Basically in this problem when user will make wrong request like robots.txt then we simply have to deny them.
        We can deny then using errorhandler and abort(404) but here more specifically robots.txt page is denied only.
        
        Check output at:-http://localhost:5000/robots.txt
   Quest 6. Render an HTML page at http://localhost:8080/html or an image at http://localhost:8080/image.
        
    Sol:- 
         Solution at:- image.py html.html
          In this problem we have to reponse with an image and in another problem response should be a html file.
          So simply send_file and render_tenplate class from package flask is used to do this work.
          Chack output at:-http://localhost:5000/html and http://localhost:5000/image
          
   Ques 7. A text box at http://localhost:8080/input which sends the data as POST to any endpoint of your choice. This endpoint should log the received the received to endpoint.
           
    Sol:- 
        Soluton at:- input.py and input.html
          In this problem we have taken  input from user in form and using POST method send to url-http://127.0.0.1:5000/AAA
          there we just print that data to console
          
          check output at:- http://localhost:5000/input

END.
        
            
   
        
        
        

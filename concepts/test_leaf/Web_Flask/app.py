from flask import Flask, render_template,request  # Import Flask

app = Flask(__name__)  # Create an app instance


@app.route("/", methods=['GET'])  # Set the endpoint
def login_page():  # Call this method
    return render_template("login_page.html")       # render_template to load html page


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':   # If there it is a POST method add this logic in app.py
        fname = request.form.get('FNAME')   # Get the data from html "name" attribute by using the imported "request" class and store it in fname
        lname = request.form.get('LNAME')
        email = request.form.get('EMAIL')
        pwd = request.form.get('PWD')
        print(fname,lname,email,pwd)
    return render_template("Register.html")         # render_template to Register html page


if __name__ == "__main__":
    app.run(debug=True)
import smtplib, ssl
from flask import Flask

app = Flask(__name__)  # Create an app instance


@app.route("/")  # Set the endpoint
def login_page():  # Call this method
    return """<html>
    <head></head>
    <body>
    <h2>LEARN FLASK</h2>    
    </body>    
    </html>"""  # Returns text


if __name__ == "__main__":
    app.run(debug = True)
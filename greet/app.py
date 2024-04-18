from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    """Returns Welcome!"""
    html = """
    <html>
       <body>
       <h1>Welcome!</h1>
       </body>
    </html>
    """
    return html

@app.route("/welcome/home")
def welcome_home():
    """Returns Welcome Home!"""
    html = """
    <html>
       <body>
       <h1>Welcome Home!</h1>
       </body>
    </html>
    """
    return html

@app.route("/welcome/back")
def welcome_back():
    """Returns Welcome Back!"""
    html = """
    <html>
       <body>
       <h1>Welcome Back!</h1>
       </body>
    </html>
    """
    return html
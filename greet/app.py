from flask import Flask

app=Flask(__name__)

@app.get("/welcome")
def welcome():
    response = """
    <html>
        <body>
            <h1>welcome</h1>
        </body>
        </html>
    """
    return response

@app.get("/welcome/home")
def welcome_home():
    response = """
    <html>
        <body>
            <h1>welcome home</h1>
        </body>
    </html>
    """
    return response

@app.get("/welcome/back")
def welcome_back():
    response = """
    <html>
        <body>
            <h1>welcome back</h1>
        </body>
    </html>
     """
    return response
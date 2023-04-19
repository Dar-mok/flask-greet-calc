from flask import Flask, request

import operations

app=Flask(__name__)

@app.get("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"<h1>{operations.add(a,b)}</h1>"

@app.get("/sub")
def sub():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"<h1>{operations.sub(a,b)}</h1>"

@app.get("/mult")
def mult():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"<h1>{operations.mult(a,b)}</h1>"

@app.get("/div")
def div():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"<h1>{operations.div(a,b)}</h1>"
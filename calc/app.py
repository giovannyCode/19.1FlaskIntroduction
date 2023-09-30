from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    """Returns addition of two numbers."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operations.add(a,b)
    html = f"<html><body><h1>The restult is {result} </h1></body></html>"
    return html

@app.route('/sub')
def sub():
    """Returns addition of two numbers."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operations.sub(a,b)
   
    return str(result)

@app.route('/mult')
def mult():
    """Returns addition of two numbers."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operations.mult(a,b)
  
    return str(result)

@app.route('/div')
def div():
    """Returns addition of two numbers."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operations.div(a,b)
    return str(result)
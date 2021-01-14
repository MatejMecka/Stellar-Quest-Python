from flask import Flask, Response

app = Flask(__name__, static_url_path='')

with open('stellar.toml') as f:
    file = f.read()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/.well-known/stellar.toml')
def stellar_toml():
    resp = Response(file) 
    resp.headers["Content-Type"] = "text/plain"
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

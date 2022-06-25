
import flask
import socket

app = flask.Flask(__name__)

@app.route("/")
def index():
    ip_address = flask.request.remote_addr
    server_ip = socket.gethostbyname(socket.gethostname())
    return f"Requester IP: {ip_address} server ip: {server_ip}"

import flask
import socket

app = flask.Flask(__name__)

@app.route("/")
def index():
    ip_address = flask.request.remote_addr
    server_ip = socket.gethostbyname(socket.gethostname())
    #fqdn = socket.getfqdn()
    return f"Requester IP: {ip_address} server ip: {server_ip}"


app.run(host="0.0.0.0", port=5000)
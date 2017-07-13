import eventlet

# Monkeypatch all the things :S
eventlet.monkey_patch()


from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
sio = SocketIO(app)


@app.route("/")
def index():
  """
  Just return 'It works!'
  """
  return "It works!"

if __name__ == '__main__':
  sio.run(app, host="0.0.0.0", port=5000, debug=True)
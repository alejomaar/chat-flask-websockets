from flask import Flask, render_template
from flask_socketio import SocketIO,send, emit
from werkzeug import debug

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,logger=True, engineio_logger=True,cors_allowed_origin="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def connect():
    print('Client connected')

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')

@socketio.on("message")
def handleMessage(message_data):
    emit("new_message",message_data,broadcast=True, include_self=False)
    #broadcast=True,
    
if __name__ == "__main__":
    socketio.run(app,debug=True)
    #, host='0.0.0.0', port=5004

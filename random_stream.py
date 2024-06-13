from flask import Flask, render_template
from flask_socketio import SocketIO
import eventlet
import random
import time

# Create Flask app and configure SocketIO
app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/')
def index():
    return render_template('index.html')

def generate_random_numbers():
    while True:
        number = random.randint(0, 100)
        print(f"Generated number: {number}")  # For debugging
        socketio.emit('new_number', {'number': number}, namespace='/')
        time.sleep(1)

if __name__ == '__main__':
    # Start the background thread that generates random numbers
    socketio.start_background_task(target=generate_random_numbers)
    socketio.run(app, host='0.0.0.0', port=5000)

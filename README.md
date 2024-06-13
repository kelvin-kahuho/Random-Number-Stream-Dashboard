# Random Number Stream Dashboard

This project generates a random number every second and displays the changes on a live stream dashboard using Flask and Flask-SocketIO.

## Features

- Real-time generation of random numbers.
- Live updating dashboard displaying the random numbers.
- Simple and easy to set up.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- `pip` (Python package installer)

## Installation

1. Clone this repository or download the files.

2. Navigate to the project directory:

    ```bash
    cd path/to/your/project
    ```

3. Install the required Python packages:

    ```bash
    pip install flask flask-socketio eventlet
    ```

## Running the Application

1. Run the Flask application:

    ```bash
    python random_stream.py
    ```

2. Open your web browser and navigate to `http://localhost:5000`.

You should see the dashboard displaying a random number that updates every second.

## Project Structure

- `random_stream.py`: The main Python file that sets up the Flask server and generates random numbers.
- `templates/index.html`: The HTML template for the dashboard.

## Explanation

- **Flask**: A micro web framework used to create the web server.
- **Flask-SocketIO**: A Flask extension that enables real-time bi-directional communication between the web server and clients.
- **eventlet**: A concurrent networking library for Python that works well with `flask-socketio` for handling real-time events.
- **random.randint**: Generates a random integer between 0 and 100.
- **SocketIO.emit**: Sends the generated random number to all connected clients.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Flask-SocketIO: [https://flask-socketio.readthedocs.io/](https://flask-socketio.readthedocs.io/)
- Eventlet: [http://eventlet.net/](http://eventlet.net/)
- Socket.IO: [https://socket.io/](https://socket.io/)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

For any questions, please contact [your-email@example.com](mailto:your-email@example.com).

"""App entry point."""
from flask_app import create_app, socketio
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    # socketio.run(app, debug=True, allow_unsafe_werkzeug=True)

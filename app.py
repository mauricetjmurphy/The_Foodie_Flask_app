# Import the app variable from the app  package (__init__.py file)
from app import app

if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=5000, debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
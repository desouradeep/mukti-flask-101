# WSGI webapp using Flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """
    Homepage
    """
    return "Hello, Mukti"

if __name__ == "__main__":
    app.run(debug=True)


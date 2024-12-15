from flask import Flask
app = Flask(__name__)

@app.route("/")
def health():
    return "Hello World."

@app.route("/healthcheck")
def health():
    return "Ok"

if __name__ == "__main__":
    app.run()

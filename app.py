from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def health():
    return f"Hello World. Here's the environment variable {os.environ.get('TEST_ENV_VAR')}"

if __name__ == "__main__":
    app.run()

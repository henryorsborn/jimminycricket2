from flask import Flask
import os
app = Flask("JimminyCricket")

engine = sqlalchemy.create_engine(f"mysql://{os.environ.get('DB_USER')}@{os.environ.get('DB_HOST')}/{os.environ.get('DB_NAME')}")
db = engine.connect()

@app.route("/")
def health():
    return f"TableNames: {engine.table_names()}"

if __name__ == "__main__":
    app.run()

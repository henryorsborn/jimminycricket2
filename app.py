from flask import Flask
from sqlalchemy import event
import os, boto3
import sqlalchemy

app = Flask("JimminyCricket")

session = boto3.Session()
client = session.client('rds')

dbuser = os.environ.get('DB_USER')
dbhost = os.environ.get('DB_HOST')
dbname = os.environ.get('DB_NAME')
dbport = os.environ.get('DB_PORT')
region = os.environ.get('REGION')

engine = sqlalchemy.create_engine(f"mysql://{dbuser}@{dbhost}/{dbname}")
db = engine.connect()


@event.listens_for(engine, "do_connect")
def provide_token(dialect, conn_rec, cargs, cparams):
    cparams["token"] = get_db_token()


def get_db_token():
    return client.generate_db_auth_token(
        DBHostname=dbhost,
        Port=dbport,
        DBUsername=dbuser,
        Region=region)


@app.route("/")
def health():
    return f"TableNames: {db.execute('SHOW TABLES').fetchall()}"


if __name__ == "__main__":
    app.run()

from flask import Flask
from sqlalchemy import event
import os, boto3
import sqlalchemy

app = Flask("JimminyCricket")

dbuser = os.environ.get('DB_USER')
dbhost = os.environ.get('DB_HOST')
dbname = os.environ.get('DB_NAME')
dbport = os.environ.get('DB_PORT')
region = os.environ.get('REGION')

engine = sqlalchemy.create_engine("mysql:///")
db = engine.connect()


@event.listens_for(engine, "do_connect")
def provide_token(dialect, conn_rec, cargs, cparams):
    client = boto3.client("rds")
    token = client.generate_db_auth_token(DBHostname=dbhost, Port=dbport, DBUsername=dbuser, Region=region)
    # set up db connection parameters, alternatively we can get these from boto3 describe_db_instances
    cparams['host'] = dbhost
    cparams['port'] = dbport
    cparams['user'] = dbuser
    cparams['password'] = token
    cparams['database'] = dbname


@app.route("/")
def health():
    return f"TableNames: {db.execute('SHOW TABLES').fetchall()}"


if __name__ == "__main__":
    app.run()

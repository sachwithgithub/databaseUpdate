from flask import Flask,request
from db_operation import db_operations

application = Flask(__name__)
db_operator = db_operations()

@application.route("/insert",methods=["POST"])
def insert_table():
    return db_operator.insert(request)


@application.route("/update",methods=["POST"])
def update():
    return db_operator.update(request)


@application.route("/delete",methods=["POST"])
def delete():
    return db_operator.delete(request)


@application.route("/query",methods=["GET"])
def query():
    return db_operator.query()


if __name__=="__main__":
    application.run(host='0.0.0.0')

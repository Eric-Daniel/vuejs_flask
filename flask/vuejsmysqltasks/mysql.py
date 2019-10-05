from flask import Flask, jsonify, request
from flask_mysqldb import flask_mysqldbfrom flask_cors import flask_cors

app = Flask(__naem__)

app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] == 'db_tasks'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
CORS(app)


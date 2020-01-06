from app import app
from flaskext.mysql import MySQL
from flask_mysqldb import MySQL
import mysql.connector
import pymysql
from flask_mysqldb import MySQL



mysql = MySQL(app)
 
# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'stock_exchange'
app.config['MYSQL_HOST'] ='localhost'
mysql.init_app(app)
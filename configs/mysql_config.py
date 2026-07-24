import os

MYSQL_HOST = os.getenv("MYSQLHOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQLPORT", 3306))
MYSQL_DATABASE = os.getenv("MYSQLDATABASE", "weather_db")
MYSQL_USERNAME = os.getenv("MYSQLUSER", "root")
MYSQL_PASSWORD = os.getenv("MYSQLPASSWORD", "2006")
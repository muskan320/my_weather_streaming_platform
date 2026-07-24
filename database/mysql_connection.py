import mysql.connector

from configs.mysql_config import (

    MYSQL_HOST,

    MYSQL_PORT,

    MYSQL_DATABASE,

    MYSQL_USERNAME,

    MYSQL_PASSWORD

)

connection = mysql.connector.connect(

    host=MYSQL_HOST,

    port=MYSQL_PORT,

    database=MYSQL_DATABASE,

    user=MYSQL_USERNAME,

    password=MYSQL_PASSWORD

)

cursor = connection.cursor(dictionary=True)
import mysql.connector

#conectando mysql

conexao = mysql.connector.connect (
    host = "127.0.0.1",
    user = "root",
    password = "HTTPSENRICO%",
    database =  "delivery_db"
)

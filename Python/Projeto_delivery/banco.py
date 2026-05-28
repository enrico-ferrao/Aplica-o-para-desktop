import mysql.connector

#conectando mysql

conexao = mysql.connector.connect(
    host = "deliverydb-enricogferrao-d95a.l.aivencloud.com",
    port = 12884,
    user = "avnadmin",
    password = ".....",
    database = "defaultdb"
)

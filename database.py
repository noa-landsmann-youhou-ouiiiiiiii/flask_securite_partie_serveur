import pymysql

def get_connection():
    try:
        connection = pymysql.connect(
            host="mysql-noalam.alwaysdata.net",
            user="noalam",
            password="l%S2BC1el",
            database="noalam_securite_nn",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print("Erreur MySQL :", e)
        return None
import pymysql

def get_connection():
    try:
        connection = pymysql.connect(
            host="",
            user="",
            password="",
            database="",
            charset=" ",
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print("Erreur MySQL :", e)
        return None
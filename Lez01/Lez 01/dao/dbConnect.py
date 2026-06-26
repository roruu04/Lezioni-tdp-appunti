import mysql


class DBConnect:
    @classmethod
    def getConnection(self):
        try:
            cnx = mysql.connector.connect(
                user='root',
                password='bobabibibubu',
                host = "127.0.0.1",
                database = "sw.gestionale"
            )
            return cnx
        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al db")
            print(err)
            return None
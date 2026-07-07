import pathlib

import mysql.connector
#generalmente all'esame viene data
class DBConnect:
    _mypool=None
    def __init__(self):
        #per implementare pattern singletone e impedire al chiamante di creare istanza di classe
        raise RuntimeError("Attenzione, non devi creare un'istanza di questa classe, usa i metodi di classe")

    @classmethod
    def getConnection(cls):
        if cls._mypool is None:
            try:
                #cnx = mysql.connector.connect(
                #    user='root',
                #   password='bobabibibubu',
                #   host = "127.0.0.1",
                #   database = "sw.gestionale"
                #)
                cls._mypool = mysql.connector.pooling.MySQLConnectionPool(
                    #user='root',
                    #password='bobabibibubu',
                    #host = "127.0.0.1",
                    #database = "sw.gestionale",
                    pool_size = 3,
                    pool_timeout = "myPool",
                    option_files = f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"

                )
                return cls._mypool.get_connection()
            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None
        else:
            return cls._mypool.get_connection()
import psycopg2
import Crypto


class PostgresDAO():
    def __init__(self):
        self.conn = psycopg2.connect("dbname='magodaprogramacao' user='postgres' host='localhost' password='123456'")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def insertUsuario(self):
        self.cur.execute("INSERT INTO USUARIO(EMAIL, PASSAWORD) VALUES('kkkkkk','kkkkkkkk')")

    def selectUsuario(self):
        self.cur.execute("""SELECT * from usuario""")
        rows = self.cur.fetchall()
        for row in rows:
            print("   ", row)

    def updateUsuarioEmail(self, email, idUsuario):
        self.cur.execute("""update usuario set email = %s where id_usuario = %d """, (email, idUsuario))

    def updateUsuarioNome(self, nome, idUsuario):
        self.cur.execute("""update usuario set nome = %s where id_usuario = %d """, (nome, idUsuario))

    def updateUsuarioSenha(self, nome, idUsuario):
        self.cur.execute("""update usuario set nome = %s where id_usuario = %d """, (nome, idUsuario))

    def deleteUsuario(self, idUsuario):
        self.cur.execute("""delete from usuario where = %d """, (idUsuario))

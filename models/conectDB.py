import psycopg2
from pymongo import MongoClient

class PostgresDAO():
    def __init__(self):
        self.conn = psycopg2.connect("dbname='magodaprogramacao' user='postgres' host='localhost' password='123456'")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def insertUsuario(self, name, cpf ,email,password):
        self.cur.execute("""INSERT INTO applicant(name_candidate, cpf ,EMAIL_applicant,PASSAWORD)VALUES((?),(?),(?),(?))""", (name, cpf ,email,password))

    def selectUsuario(self):
        self.cur.execute("""SELECT * from applicant""")
        rows = self.cur.fetchall()
        for row in rows:
            print("   ", row)

    def updateUsuarioEmail(self, email, idUsuario):
        self.cur.execute("""update applicant set email_applicant = %s where id_applicant = %d """, (email, idUsuario))

    def updateUsuarioNome(self, nome, idUsuario):
        self.cur.execute("""update applicant set name_candidate = %s where id_applicant = %d """, (nome, idUsuario))

    def updateUsuarioSenha(self, password, idUsuario):
        self.cur.execute("""update applicant set password = %s where id_applicant = %d """, (password, idUsuario))

    def deleteUsuario(self, idUsuario):
        self.cur.execute("""delete from applicant where  id_applicant = %d """, (idUsuario))

    def updateUsuarioNome(self, cpf, idUsuario):
        self.cur.execute("""update applicant set cpf = %s where id_applicant = %d """, (cpf, idUsuario))

    def insertCompany(self, name_company,trade_c,address,name_responsible,email,password_company,descri,cnpj):
        self.cur.execute("""insert into
        company(name_company,trade_c,address,name_responsible,email,password_company,descri,cnpj)
        values ((?),(?),(?),(?),(?),(?),(?),(?)
        )""", (name_company,trade_c,address,name_responsible,email,password_company,descri,cnpj))


    def updateCompanyPassword(self,password,id_company):
        self.cur.execute("""update company set password=%s where id_company = %d """, (password,id_company))


    def updateCompanyName(self, id_company, name):
        self.cur.execute("""update company set name_company=%s where id_company = %d """, (nzme,id_company))


    def updateCompanyCNPJ(self,cnpj,id_company):
        self.cur.execute("""update company set cnpj=%d where id_company = %d """, (cnpj,id_company))

    def updateCompanyEmail(self,email,id_company):
        self.cur.execute("""update company set email=%s where id_company = %d """, (email, id_company))

    def updateCompanyResponsible(self,id_company,name_responsible):
        self.cur.execute("""update company set email=%s where id_company = %d """, (name_responsible, id_company))

    def updateCompanyTrandingName(self,id_company,trade_c):
        self.cur.execute("""update company set trade_c=%s where id_company = %d """, (trade_c, id_company))

    def updateCompanySize(self,id_company,size_company):
        self.cur.execute("""update company set email=%s where id_company = %d """, (size_company, id_company))

    def listCompany(self):
        list_empresa = self.cur.execute("select * from company")
        for lista in list_empresa:
            print("  " + lista)

    def deleteCompany(self, id_company):
        self.cur.execute("delete from company where id_comany=%d", (id_company))



class MongodbDOA():
    def __init__(self):
        self.cliente = MongoClient()
        self.db = self.cliente.magodaprogramacao
        self.cursorCurriculum = self.db.curriculum.find()
        self.cursorWave = self.db.wave.find()

    def insertCurriculo(self, insertJSON):
        result = self.db.cursorCurriculum.insert_one(insertJSON)
        print(result.inserted_id)

    def listCurriculo(self):

        for doc in self.cursorCurriculum:
            print(doc)

    def searchCurriculo(self, searchJSON):
        self.cursorCurriculum.find(searchJSON)


    def updateCurriculo(self):
        self.cursorCurriculum.update()

    def deleteCurriculo(self, id_curriculum):
        self.cursorCurriculum.remove()

    def filterCurrriculo(self):
        self.cursorCurriculum.

    def insertJob(self,insertJSON):
        self.cursorWave.insert_one(insertJSON)

    def updateJob(self):
        self.cursorWave.update()

    def deleteJob(self):
        self.cursorWave.remove()

    def listJob(self):
        self.cursorWave.find()

    def searchJob(self):
        self.cursorWave.find()

    def filterJob(self):
        self.cursorWave.

kkk = MongodbDOA()

kkk.insertCurriculo()
kkk.listCurriculo()
from flask import Flask, render_template
from models.conectDB import MongodbDOA, PostgresDAO
app = Flask(__name__)
app._static_folder = "/templates"

pgDB = PostgresDAO()

@app.route("/")
def main():
    pgDB.insertCompany(),
    return render_template('index.html')

@app.route("/cadastro")
def singup():
    pass
@app.route("/login")
def login():
    pass
@app.route('/admin')





if __name__ == "__main__":
    app.run()
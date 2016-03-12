from flask import Flask, render_template
from models.mysqlConec import insertCadastro
app = Flask(__name__)
app._static_folder = "/templates"


@app.route("/")
def main():
    insertCadastro()
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
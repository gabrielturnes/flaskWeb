from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

SECRET_KEY = "string aleatória" #proteção contra alguns ataques
app.secret_key = SECRET_KEY

engine = create_engine("sqlite:///lab05-flask.sqlite")
Session = sessionmaker(bind=engine)
Base = automap_base()
Base.prepare(engine, reflect=True)

Pessoa = Base.classes.Pessoa
Telefones = Base.classes.Telefones

@app.route('/listar')
def listar_pessoas():
    sessionSQL = Session()
    pessoas = sessionSQL.query(Pessoa).all()
    sessionSQL.close()
    return render_template('listar.html', titulo="Listar", lista_pessoas = pessoas)

@app.route('/inicio')
@app.route('/')
def inicio():
    return render_template('index.html',titulo="Início")

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html',titulo="Cadastrar")

@app.route('/editar')
def editar():
    sessionSQL = Session()
    pessoa = sessionSQL.query(Pessoa).filter(id==id())
    sessionSQL.close()
    return render_template('editar.html',titulo="Editar", dados_pessoa = pessoa)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

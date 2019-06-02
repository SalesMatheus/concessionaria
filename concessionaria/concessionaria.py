# Matheus Carvalho Sales



# Importando bibliotecas
from flask import Flask, request, render_template, redirect, url_for
from flaskext.mysql import MySQL
from bd import *


# Instanciando a app Flask
app = Flask(__name__)
# Instanciar o objeto MySQL
mysql = MySQL()
# Ligar o MYSQL ao Flask
mysql.init_app(app)

# configuracao do bd
config(app)

# Rotas para o index
@app.route('/')
@app.route('/<idlogin>')
def principal(idlogin=None):
    return render_template('index.html', idlogin = idlogin)

# Rota para /login
@app.route('/login')
def login():
    return render_template('login.html')

# Rota para /usuario
@app.route('/usuario/<idlogin>')
def usuario(idlogin):
    return render_template('usuario.html', idlogin=idlogin)

# Rota para /usuario_listar
@app.route('/usuario_listar/<idlogin>')
def usuario_listar(idlogin):

    # recupera conexao e cursor
    conn, cursor = get_db(mysql)

    return render_template('usuario_listar.html', idlogin=idlogin, usuarios = listar_usuario(cursor))

# rota para salvar novo usuario
@app.route('/novo_usuario/<idlogin>' , methods=['GET','POST'])
def salvar_usuario(idlogin):

    # recuperar os parametros
    nome = request.form.get('nome')
    login = request.form.get('login')
    senha = request.form.get('senha')

    if(nome and login and senha):
        # recupera conexao e cursor
        conn, cursor = get_db(mysql)

        # Inserindo novo usuario no banco de dados
        usuario_cadastrar(conn, cursor, nome, login, senha)

        return render_template('usuario_listar.html', usuarios = listar_usuario(cursor), idlogin=idlogin)
    else:
        return redirect(url_for('static', filename='404.html', idlogin=idlogin))

# rota para excluir usuario
@app.route('/usuario_del/<idlogin>' , methods=['GET','POST'])
def usuario_delete(idlogin):

    if(idlogin):
        # recupera conexao e cursor
        conn, cursor = get_db(mysql)

        # Inserindo novo usuario no banco de dados
        usuario_excluir(conn, cursor, idlogin)

        return render_template('usuario_listar.html', usuarios = listar_usuario(cursor), idlogin=idlogin)
    else:
        return redirect(url_for('static', filename='404.html', idlogin=idlogin))
# Rota para /adm
@app.route('/adm', methods=['GET','POST'])
def log():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        # Obtendo o cursor para acessar o BD
        cursor = mysql.get_db().cursor()

        # Obtendo o idlogin
        idlogin = get_idlogin(cursor, login, senha)

        # Verificar a senha
        if idlogin is None:
            return render_template('login.html',erro='Login/senha incorretos!')
        else:
            return render_template('index.html', idlogin = idlogin[0])

    else:
        return render_template('login.html', erro='Método incorreto. Use POST!')

# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)
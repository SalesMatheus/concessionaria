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

config(app)

# Rota para /
@app.route('/')
def principal():
    return render_template('index.html')

# Rota para /login
@app.route('/login')
def login():
    return render_template('login.html')

# Rota para /usuario
@app.route('/usuario/<idlogin>')
def usuario(idlogin):
    return render_template('usuario.html', idlogin=idlogin)

# rota para salvar a alteração
@app.route('/novo_usuario/<idlogin>' , methods=['GET','POST'])
def salvar_url(idlogin):

    # recuperar os parametros
    nome = request.form.get('nome')
    login = request.form.get('login')
    senha = request.form.get('senha')

    # recupera conexao e cursor
    conn, cursor = get_db(mysql)

    # Inserindo nova url no banco de daods
    usuario_cadastrar(conn, cursor, nome, login, senha)

    # redirecionando para index com botão de listagem de urls
    return render_template('index.html', idlogin=idlogin)

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
            # Obtendo o cursor para acessar o BD
            cursor = mysql.get_db().cursor()
            #return redirect(url_for('static', filename='login.html'))
            return render_template('index.html', idlogin = get_idlogin(cursor, login, senha))

    else:
        return render_template('login.html', erro='Método incorreto. Use POST!')

# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)
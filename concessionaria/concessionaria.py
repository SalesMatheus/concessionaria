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

# Configurando o acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'banco'

# Rota para /
@app.route('/')
def principal():
    return render_template('index.html')


# Rota para /login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        # Obtendo o cursor para acessar o BD
        cursor = mysql.get_db().cursor()

        # Obtendo o idlogin
        idlogin = get_idlogin(cursor, login, senha)

        # Verificar a senha
        if idlogin is None:
            return redirect(url_for('static', filename='login.html', erro='Login/senha incorretos!'))
            #return render_template('static/login.html', erro='Login/senha incorretos!')
        else:
            # Obtendo o cursor para acessar o BD
            #cursor = mysql.get_db().cursor()
            return redirect(url_for('static', filename='login.html'))
            #return render_template('static/login.html', erro='Login/senha incorretos!')

    else:
        return render_template('login.html', erro='Método incorreto. Use POST!')

# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)
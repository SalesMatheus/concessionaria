# Matheus Carvalho Sales
# 21804995


# Importando bibliotecas
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
#from bd import *


# Instanciando a app Flask
app = Flask(__name__)
# Instanciar o objeto MySQL
mysql = MySQL()
# Ligar o MYSQL ao Flask
mysql.init_app(app)

# Configurando o acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'faculdade'

# Rota para /
@app.route('/')
def principal():
    return render_template('index.html')

# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)
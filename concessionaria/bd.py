from flaskext.mysql import MySQL

# função para configurar o acesso a banco
def config(app):
    # Configurando o acesso ao MySQL
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'concessionaria'

# Retorna conexao e cursor
def get_db(mysql):
    # Obtendo o cursor para acessar o BD
    conn = mysql.connect()
    cursor = conn.cursor()

    return conn, cursor

#insere usuario
def usuario_cadastrar(conn,cursor, nome, usuario, login):
    print(nome)
    print(usuario)
    print(login)
    cursor.execute(f'INSERT INTO `concessionaria`.`usuario` (`nome`,`login`, `senha`) VALUES ("{nome}", "{usuario}" ,"{login}")')
    conn.commit()


# Função validar login
def get_idlogin(cursor, login, senha):
    # Executar o sql
    cursor.execute(f'SELECT id_usuario FROM usuario WHERE login = "{login}" AND senha = "{senha}"')

    # Recuperando o retorno do BD
    idlogin = cursor.fetchone()

    # Fechar o cursor
    cursor.close()

    # Retornar o idlogin
    return idlogin[0]
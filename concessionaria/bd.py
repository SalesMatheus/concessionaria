# Função validar login
def get_idlogin(cursor, login, senha):
    # Executar o sql
    cursor.execute(f'select id_usuario from usuario where login = "{login}" and senha = "{senha}"')

    # Recuperando o retorno do BD
    idlogin = cursor.fetchone()

    # Fechar o cursor
    cursor.close()

    # Retornar o idlogin
    return idlogin[0]
# Função validar login
def get_idlogin(cursor, login, senha):
    # Executar o sql
    cursor.execute(f'select idlogin from clientes where login = "{login}" and senha = "{senha}"')

    # Recuperando o retorno do BD
    idlogin = cursor.fetchone()

    # Fechar o cursor
    cursor.close()

    # Retornar o idlogin
    return idlogin[0]
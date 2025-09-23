import pymysql.cursors
from ex004_treats import corretor_entradas

def conexao():
    """
    Faz a conexão do servidor do banco de dados com a API
    con: Variável que armazena a conexão
    """

    con = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='livraria',
        cursorclass=pymysql.cursors.DictCursor
    )
    return con

def get_from_tbl_livros(option:str) -> int:
    """
    Lista alguns livros específicos cadastrados
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    enter: Guarda a entrada do usuário
    titulo: Guarda o titulo
    id_: Guarda o id do livro
    autor: Guarda o autor do livro
    sql: Guarda o comando do banco de dados
    res: Resultado em um dict
    """
    con = conexao()
    cursor = con.cursor()

    if 'titulo' in option:
        titulo = corretor_entradas('Titulo: ')
        sql = 'SELECT id, titulo, autor FROM tbl_estante WHERE titulo = (%s)'
        cursor.execute(sql, titulo)
    elif 'id' in option:
        id_ = corretor_entradas('ID: ')
        sql = 'SELECT id, titulo, autor FROM tbl_estante WHERE id = (%s)'
        cursor.execute(sql, id_)
    else:
        autor = corretor_entradas('Autor: ')
        sql = 'SELECT id, titulo, autor FROM tbl_estante WHERE autor = (%s)'
        cursor.execute(sql, autor)

    try:
        res = cursor.fetchall()
        print(f'Título: {res[0]['titulo']} /// Autor: {res[0]['autor']} /// ID: {res[0]['id']}')
        return res[0]['id']
    finally:
        con.close()
        cursor.close()


def get_from_tbl_users(option: str) -> list:
    """
    Lista alguns usuários específicos cadastrados
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    enter: Guarda a entrada do usuário
    nome: Guarda o nome do usuário
    cpf: Guarda o cpf do usuário
    sql: Guarda o comando do banco de dados
    res: Resultado em um dict
    """
    con = conexao()
    cursor = con.cursor()
    try:
        if 'nome' in option:
            nome = input('Nome: ')
            sql = 'SELECT nome, cpf FROM tbl_users WHERE nome = (%s)'
            cursor.execute(sql, nome)
        else:
            cpf = corretor_entradas('CPF: ')
            sql = 'SELECT nome, cpf FROM tbl_users WHERE cpf = (%s)'
            cursor.execute(sql, cpf)

        res = cursor.fetchall()
        print(f'Nome: {res[0]['nome']} /// CPF: {res[0]['cpf']}')
        return res[0]['cpf']
    except pymysql.Error as e:
        print('Erro ao mostrar informações', e)
        con.rollback()
    finally:
        con.close()
        cursor.close()

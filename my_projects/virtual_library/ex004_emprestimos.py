import pymysql.cursors
from ex004_users import conexao
from ex004_livros import listar_some
from datetime import date
from ex004_users import listar_user
from my_projects.virtual_library.ex004_extras import get_from_tbl_users
from my_projects.virtual_library.ex004_extras import get_from_tbl_livros


def emprestimos_livros():
    """
    Sistema de emprestimos, incompleto ainda
    con: Armazena a conexão com o servidor
    cursor: Metódo que executa os comandos no banco de dados
    id_livro: Id do livro que vai ser pego ou devolvido
    id_user: Id do usuário que vai pegar ou devolver um livro
    data_emprestimo: Data da cautela
    sql: Comando que vai ser executado no banco de dados
    """
    con = conexao()
    cursor = con.cursor()
    try:
        print('-' * 20)
        print('ID do Livro e CPF do usuário')
        print('-' * 20)

        livro_id = get_from_tbl_livros('id')
        usuario_id = get_from_tbl_users('cpf')

        sql = "INSERT INTO tbl_emprestimos (usuario_id, livro_id, condicao) VALUES (%s, %s, %s)"
        cursor.execute(sql, (usuario_id, livro_id, 1))
        con.commit()
    except pymysql.Error as e:
        print('Erro no emprestimo', e)
        con.rollback()
    finally:
        print('Empréstimo feito com sucesso!')
        con.close()
        cursor.close()

def ver_emprestimos(s):
    return False

def devolucao_livro():
    con = conexao()
    cursor = con.cursor()

    usuario_id = get_from_tbl_users('cpf')
    id_transacao = ver_emprestimos(usuario_id)

    sql = 'DELETE FROM tbl_emprestimos WHERE id=(%s)'
    cursor.execute(sql, id_transacao)
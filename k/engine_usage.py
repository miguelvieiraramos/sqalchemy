"""
    Engine

    create_engine() constroi uma factory de conexões ao banco de dados.
    future quer dizer que usaremos funcionalidades da versão 2.0
"""


from sqlalchemy import create_engine


engine = create_engine("sqlite:///some.db", future=True)

def get_conn():
    return engine.connect()

"""Arquivo auxiliar com conexao com Mysql."""
from sqlalchemy import create_engine


class MysqlConnection:
    """Classe de conexao com mysql."""

    def connect(self):
        """Cria um engine e retorna."""
        return create_engine(
            'mysql://mydb:mydb@mysqletl_fee_db_1:3306/mydb', echo=False
        )

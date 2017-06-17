"""."""
import pandas as pd
import os
from mysql_connection import MysqlConnection
import abc


class BaseImport:
    """Classe base para importacoes."""

    def __init__(self):
        """."""
        self.__db_engine = MysqlConnection().connect()
        self.__project_home = os.environ['PROJECT_HOME']

    @property
    def table_name(self):
        """Propriedade 'table_name'."""
        return self.__table_name

    @table_name.setter
    def table_name(self, val):
        self.__table_name = val

    def read(self, datafile_name, index_column, column_names):
        """Leitura do CSV."""
        self.df = pd.read_csv(
            self.__project_home + '/datafiles/' + datafile_name,
            index_col=index_column,
            header=1,
            names=column_names,
            delimiter=';'
        )

        return self.df

    def save(self):
        """Salvar no banco."""
        self.df.to_sql(
            name=self.__table_name, con=self.__db_engine, schema='mydb',
            if_exists='append', index=True
        )

    @abc.abstractmethod
    def run(self):
        """Executar todos os processos."""

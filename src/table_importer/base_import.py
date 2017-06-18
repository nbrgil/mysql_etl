"""Importador generico."""
import os
from util.mysql_connection import MysqlConnection
import abc


class BaseImport:
    """Classe base para importacoes."""

    def __init__(self):
        """."""
        self.__db_engine = MysqlConnection().connect()
        self.__project_home = os.environ['PROJECT_HOME']

    @property
    def db_engine(self):
        """Propriedade 'table_name'."""
        return self.__db_engine

    @db_engine.setter
    def db_engine(self, val):
        self.__db_engine = val

    @property
    def table_name(self):
        """Propriedade 'table_name'."""
        return self.__table_name

    @table_name.setter
    def table_name(self, val):
        self.__table_name = val

    @property
    def reader(self):
        """Propriedade 'reader'."""
        return self.__reader

    @reader.setter
    def reader(self, val):
        self.__reader = val

    def read(self):
        """Leitura do CSV."""
        self.df = self.reader.read()

    def save(self):
        """Salvar no banco."""
        self.df.to_sql(
            name=self.__table_name, con=self.__db_engine, schema='mydb',
            if_exists='append', index=False
        )

    @abc.abstractmethod
    def transform(self):
        """Efetua Transformacoes necessarias antes de salvar."""

    def run(self):
        """Executar todos os processos."""
        self.read()
        self.transform()
        self.save()

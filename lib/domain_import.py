"""."""
import pandas as pd
import os
from mysql_connection import MysqlConnection
import abc


class DomainImport:
    """."""

    def __init__(self):
        """."""
        self.__db_engine = MysqlConnection().connect()
        self.__project_home = os.environ['PROJECT_HOME']

    @property
    def column_names(self):
        """."""
        return self.__column_names

    @column_names.setter
    def column_names(self, val):
        """."""
        self.__column_names = val

    @property
    def index_column(self):
        """."""
        return self.__index_column

    @index_column.setter
    def index_column(self, val):
        self.__index_column = val

    @property
    def table_name(self):
        """."""
        return self.__table_name

    @table_name.setter
    def table_name(self, val):
        self.__table_name = val

    @property
    def datafile_name(self):
        """."""
        return self.__datafile_name

    @datafile_name.setter
    def datafile_name(self, val):
        self.__datafile_name = val

    def read(self):
        """Leitura do CSV."""
        self.df = pd.read_csv(
            self.__project_home + '/datafiles/account.csv',
            index_col=self.__index_column,
            header=1,
            names=self.__column_names,
            delimiter=';'
        )

        return self.df

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""

    def save(self):
        """Salvar no banco."""
        self.df.to_sql(
            name=self.__table_name, con=self.__db_engine, schema='mydb',
            if_exists='append', index=True
        )

    def run(self):
        """Executar todos os processos."""
        self.read()
        self.transform()
        self.save()

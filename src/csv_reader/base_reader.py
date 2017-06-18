"""."""
from util.mysql_connection import MysqlConnection
import os
import pandas as pd
import abc


class BaseReader:
    """Classe base para leitura de csv."""

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
    def datafile_name(self):
        """."""
        return self.__datafile_name

    @datafile_name.setter
    def datafile_name(self, val):
        self.__datafile_name = val

    @property
    def df(self):
        """."""
        return self.__df

    @df.setter
    def df(self, val):
        self.__df = val

    def read(self):
        """Leitura do CSV."""
        self.__index_column = None
        self.__df = pd.read_csv(
            self.__project_home + '/datafiles/' + self.__datafile_name,
            index_col=self.__index_column,
            header=0,
            names=self.__column_names,
            delimiter=';'
        )
        self.transform()
        return self.__df

    @abc.abstractmethod
    def transform(self):
        """Aplicar transformacoes no arquivo."""

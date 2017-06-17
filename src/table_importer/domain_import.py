"""."""
import abc
from base_import import BaseImport


class DomainImport(BaseImport):
    """."""

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

    def read(self):
        """Leitura do CSV."""
        return super().read(
            self.__datafile_name,
            self.__index_column,
            self.__column_names
        )

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""

    def run(self):
        """Executar todos os processos."""
        self.read()
        self.transform()
        self.save()

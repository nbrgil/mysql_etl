"""Importador generico de tabelas de dominio."""
import abc
from table_importer.base_import import BaseImport


class DomainImport(BaseImport):
    """Importador generico de tabelas de dominio."""

    def read(self):
        """Leitura do CSV."""
        return super().read()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""

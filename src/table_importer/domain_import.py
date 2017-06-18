"""."""
import abc
from table_importer.base_import import BaseImport


class DomainImport(BaseImport):
    """."""

    def read(self):
        """Leitura do CSV."""
        return super().read()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""

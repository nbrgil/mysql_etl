"""Importador de contas."""
import abc
from table_importer.base_import import BaseImport
from csv_reader.account_reader import AccountReader


class AccountImport(BaseImport):
    """Importador de contas."""

    def __init__(self):
        """Construtor."""
        self.table_name = 'account'
        self.reader = AccountReader()
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar para salvar."""
        self.df.drop('v2_integration_level', axis=1, inplace=True)
        self.df.drop('negotiated_tax', axis=1, inplace=True)

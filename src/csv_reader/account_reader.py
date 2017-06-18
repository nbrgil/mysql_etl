"""Leitor de arquivos (ver datafile_name abaixo)."""
import abc
from csv_reader.base_reader import BaseReader


class AccountReader(BaseReader):
    """Leitor de arquivos."""

    def __init__(self):
        """Construtor."""
        self.datafile_name = 'account.csv'
        self.column_names = [
            'id', 'status', 'type', 'fee_type', 'has_bonus_withdraw',
            'v2_integration_level', 'negotiated_tax', 'is_transparent'
        ]
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""
        self.df.drop_duplicates(subset='id', keep='first', inplace=True)

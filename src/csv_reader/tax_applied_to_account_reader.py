"""Leitor de arquivos (ver datafile_name abaixo)."""
import abc
from csv_reader.base_reader import BaseReader


class TaxAppliedToAccountReader(BaseReader):
    """Leitor de arquivos."""

    def __init__(self):
        """Construtor."""
        self.datafile_name = 'tax_applied_to_account.csv'
        self.column_names = [
            'id', 'account_id', 'payment_form_id', 'fixed', 'percentual'
        ]
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""
        self.df.drop_duplicates(subset='id', keep='first', inplace=True)

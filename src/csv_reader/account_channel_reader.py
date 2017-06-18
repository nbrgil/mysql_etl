"""Leitor de arquivos (ver datafile_name abaixo)."""
import abc
from csv_reader.base_reader import BaseReader


class AccountChannelReader(BaseReader):
    """Leitor das contas por canal."""

    def __init__(self):
        """Construtor."""
        self.datafile_name = 'accounts_channels.csv'
        self.column_names = [
            'channel_id', 'account_id'
        ]
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""

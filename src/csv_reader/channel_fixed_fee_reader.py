"""Leitor de arquivos (ver datafile_name abaixo)."""
import abc
from csv_reader.base_reader import BaseReader


class ChannelFixedFeeReader(BaseReader):
    """Leitor de arquivos."""

    def __init__(self):
        """Construtor."""
        self.datafile_name = 'channel_fixed_table_fee.csv'
        self.column_names = [
            'id', 'channel_id', 'payment_form_id', 'parcel_number',
            'fixed_tax_percentual', 'parcel_tax_percentual', 'fixed_tax_value'
        ]
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""
        self.df.drop_duplicates(subset='id', keep='first', inplace=True)
        self.df.drop('id', axis=1, inplace=True)

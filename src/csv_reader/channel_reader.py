"""."""
import abc
from csv_reader.base_reader import BaseReader


class ChannelReader(BaseReader):
    """."""

    def __init__(self):
        """."""
        self.datafile_name = 'channel.csv'
        self.column_names = [
            'id', 'name', 'account_id'
        ]
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""
        self.df.drop_duplicates(subset='id', keep='first', inplace=True)

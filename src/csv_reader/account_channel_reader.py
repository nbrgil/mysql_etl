"""."""
import abc
from csv_reader.base_reader import BaseReader
from csv_reader.channel_reader import ChannelReader

class AccountChannelReader(BaseReader):
    """."""

    def __init__(self):
        """."""
        self.datafile_name = 'account_channel.csv'
        self.column_names = [
            'channel_id', 'account_id'
        ]
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""
        channel_df = ChannelReader().read()

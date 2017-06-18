"""."""
import abc
from csv_reader.base_reader import BaseReader


class MemberReader(BaseReader):
    """."""

    def __init__(self):
        """."""
        self.datafile_name = 'member.csv'
        self.column_names = ['id', 'name', 'login', 'enable', 'last_name']
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""
        self.df.drop_duplicates(subset='id', keep='first', inplace=True)

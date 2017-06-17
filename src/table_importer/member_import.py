"""."""
import abc
from domain_import import DomainImport


class MemberImport(DomainImport):
    """."""

    def __init__(self):
        """."""
        self.table_name = 'member'
        self.datafile_name = 'member.csv'
        self.column_names = ['id', 'name', 'login', 'enable', 'last_name']
        self.index_column = 'id'
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""
        self.df = self.df[~self.df.index.duplicated()]


if __name__ == '__main__':
    MemberImport().run()

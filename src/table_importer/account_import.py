"""."""
import abc
from domain_import import DomainImport


class AccountImport(DomainImport):
    """."""

    def __init__(self):
        """."""
        self.table_name = 'account'
        self.datafile_name = 'account.csv'
        self.column_names = [
            'id', 'status', 'type', 'fee_type', 'has_bonus_withdraw',
            'v2_integration_level', 'negotiated_tax', 'is_transparent'
        ]
        self.index_column = 'id'
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""
        self.df.drop('v2_integration_level', axis=1, inplace=True)
        self.df.drop('negotiated_tax', axis=1, inplace=True)
        self.df = self.df[~self.df.index.duplicated()]


if __name__ == '__main__':
    AccountImport().run()

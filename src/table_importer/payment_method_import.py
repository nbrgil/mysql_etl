"""."""
import abc
from domain_import import DomainImport


class PaymentMethodImport(DomainImport):
    """."""

    def __init__(self):
        """."""
        self.table_name = 'payment_method'
        self.datafile_name = 'payment_form.csv'
        self.column_names = ['id', 'name', 'maximum_installments']
        self.index_column = 'id'
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""
        self.df = self.df[~self.df.index.duplicated()]


if __name__ == '__main__':
    PaymentMethodImport().run()

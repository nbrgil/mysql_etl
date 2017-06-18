"""."""
import abc
from csv_reader.base_reader import BaseReader


class AccountFixedFeeReader(BaseReader):
    """."""

    def __init__(self):
        """."""
        self.datafile_name = 'account_fixed_table_fee.csv'
        self.column_names = [
            'id', 'account_id', 'payment_form_id',
            'parcel_number', 'fixed_tax_percentual',
            'parcel_tax_percentual', 'fixed_tax_value'
        ]
        self.index_column = 'id'
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""
        self.df = self.df[~self.df.index.duplicated()]
        self.df['parcel_tax_percentual'] = \
            self.df['parcel_tax_percentual'].str.replace(",", ".")
        self.df['fixed_tax_value'] = \
            self.df['fixed_tax_value'].str.replace(",", ".")
        self.df['payment_form_id'] = \
            self.df['payment_form_id'].astype(int)

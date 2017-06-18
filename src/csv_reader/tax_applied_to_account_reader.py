"""."""
import abc
from csv_reader.base_reader import BaseReader


class TaxAppliedToAccountReader(BaseReader):
    """."""

    def __init__(self):
        """."""
        self.datafile_name = 'tax_applied_to_account.csv'
        self.column_names = [
            'id', 'account_id', 'payment_form_id',
            'fixed', 'antecipation_percentage',
            'one_parcel', 'between_two_and_six_parcels',
            'more_than_seven_parcels'
        ]
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar o data frame."""
        self.df.drop_duplicates(subset='id', keep='first', inplace=True)

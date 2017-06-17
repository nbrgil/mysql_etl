"""."""
import abc
from base_import import BaseImport
import numpy as np


class FeeImport(BaseImport):
    """."""

    def __init__(self):
        """."""
        self.table_name = 'fee'
        self.datafile_name = 'member.csv'
        self.column_names = ['id', 'name', 'login', 'enable', 'last_name']
        self.index_column = 'id'
        super().__init__()

    def read_account_fixed_fees(self):
        """Ler taxas de contas (acc fee type 3)."""
        self.df = self.read(
            datafile_name='account_fixed_table_fee.csv',
            index_column='id',
            column_names=[
                'id', 'account_id', 'payment_method_id',
                'installment_number', 'fixed_tax_percentual',
                'variable_fee_percentage', 'minimum_fee_value'
            ]
        )
        print(self.df)

    def transform_account_fixed_fees(self):
        """Transformar taxas de contas (acc fee type 3). ."""
        self.df['member_id'] = np.nan
        self.df['antecipation_fee_percentage'] = 1.99
        self.df.drop('fixed_tax_percentual', axis=1, inplace=True)
        # print(self.df['variable_fee_percentage'].dtype)
        # self.df['variable_fee_percentage'] = \
        #     self.df['variable_fee_percentage'].astype(float)
        # self.df.columns = [
        #     'id', 'account_id', 'payment_method_id',
        #     'installment_number', 'antecipation_fee_percentage',
        #     'variable_fee_percentage', 'minimum_fee_value', 'member_id'
        # ]
        # print(self.df.columns)

        self.df = self.df[~self.df.index.duplicated()]
        self.df.reset_index()
        self.df['variable_fee_percentage'] = \
            self.df['variable_fee_percentage'].str.replace(",", ".")
        self.df['minimum_fee_value'] = \
            self.df['minimum_fee_value'].str.replace(",", ".")

    @abc.abstractmethod
    def run(self):
        """."""
        self.read_account_fixed_fees()
        self.transform_account_fixed_fees()
        self.save()


if __name__ == '__main__':
    FeeImport().run()

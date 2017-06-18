"""."""
import abc
from table_importer.base_import import BaseImport
from csv_reader.account_fixed_fee_reader import AccountFixedFeeReader
from csv_reader.account_reader import AccountReader
from csv_reader.payment_form_reader import PaymentFormReader
from csv_reader.member_reader import MemberReader
from transformation.account_fixed_fee_transf import AccountFixedFeeTransf


class FeeImport(BaseImport):
    """."""

    def __init__(self):
        """."""
        self.table_name = 'fee'
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar para salvar."""
        tr_df = AccountFixedFeeTransf().transform(
            self.acc_fixed_fee_df,
            self.account_df,
            self.payment_form_df,
            self.member_df
        )

        tr_df = AccountFixedFeeTransf().transform(
            self.acc_fixed_fee_df,
            self.account_df,
            self.payment_form_df,
            self.member_df
        )

        self.df = tr_df

    def read(self):
        """Leitura dos CSVs."""
        self.account_df = AccountReader().read()
        self.payment_form_df = PaymentFormReader().read()
        self.acc_fixed_fee_df = AccountFixedFeeReader().read()
        self.member_df = MemberReader().read()

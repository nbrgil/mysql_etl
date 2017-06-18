"""."""
import abc
import pandas as pd
# readers
from csv_reader.account_fixed_fee_reader import AccountFixedFeeReader
from csv_reader.account_payment_fee_reader import AccountPaymentFeeReader
from csv_reader.tax_applied_to_account_reader import TaxAppliedToAccountReader
from csv_reader.account_reader import AccountReader
from csv_reader.payment_form_reader import PaymentFormReader
from csv_reader.member_reader import MemberReader
# importers
from table_importer.base_import import BaseImport
# transformation
from transformation.account_fixed_fee_transf import AccountFixedFeeTransf
from transformation.account_payment_fee_transf import AccountPaymentFeeTransf
from transformation.tax_applied_to_account_transf \
    import TaxAppliedToAccountTransf


class FeeImport(BaseImport):
    """."""

    def __init__(self):
        """."""
        self.table_name = 'fee'
        super().__init__()

    @abc.abstractmethod
    def transform(self):
        """Transformar para salvar."""
        # modelo 1
        tr1_df = TaxAppliedToAccountTransf().transform(
            self.tax_app_acc_fee_df, self.account_df, self.member_df
        )
        # modelo 2
        tr2_df = AccountPaymentFeeTransf().transform(
            self.acc_paym_fee_df, self.account_df, self.member_df
        )

        # modelo 3
        tr3_df = AccountFixedFeeTransf().transform(
            self.acc_fixed_fee_df,
            self.account_df,
            self.payment_form_df,
            self.member_df
        )

        self.df = pd.concat([tr1_df, tr2_df, tr3_df], ignore_index=True)

    def read(self):
        """Leitura dos CSVs."""
        self.account_df = AccountReader().read()
        self.payment_form_df = PaymentFormReader().read()
        self.tax_app_acc_fee_df = TaxAppliedToAccountReader().read()
        self.acc_fixed_fee_df = AccountFixedFeeReader().read()
        self.acc_paym_fee_df = AccountPaymentFeeReader().read()
        self.member_df = MemberReader().read()

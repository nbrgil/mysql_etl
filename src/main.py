"""."""
from csv_reader.account_payment_fee_reader import AccountPaymentFeeReader
from csv_reader.account_reader import AccountReader
from table_importer.account_import import AccountImport
from table_importer.member_import import MemberImport
from table_importer.payment_method_import import PaymentMethodImport
from table_importer.fee_import import FeeImport

# Readers
x = AccountPaymentFeeReader()
x.read()
x.transform()
# print(x.df)

# x = AccountReader()
# x.read()
# print(x.df)

# Importers
# AccountImport().run()
# MemberImport().run()
# PaymentMethodImport().run()
# FeeImport().run()

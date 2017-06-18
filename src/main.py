"""Arquivo principal."""
from table_importer.account_import import AccountImport
from table_importer.member_import import MemberImport
from table_importer.payment_method_import import PaymentMethodImport
from table_importer.fee_import import FeeImport

# Importers
AccountImport().run()
MemberImport().run()
PaymentMethodImport().run()
FeeImport().run()

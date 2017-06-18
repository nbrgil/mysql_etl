"""."""
from table_importer.base_import import BaseImport
from csv_reader.payment_form_reader import PaymentFormReader


class PaymentMethodImport(BaseImport):
    """."""

    def __init__(self):
        """."""
        self.table_name = 'payment_method'
        self.reader = PaymentFormReader()
        super().__init__()

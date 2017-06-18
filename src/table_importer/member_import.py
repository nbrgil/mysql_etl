"""."""
from table_importer.base_import import BaseImport
from csv_reader.member_reader import MemberReader


class MemberImport(BaseImport):
    """."""

    def __init__(self):
        """."""
        self.table_name = 'member'
        self.reader = MemberReader()
        super().__init__()

"""Importador da tabela member."""
from table_importer.base_import import BaseImport
from csv_reader.member_reader import MemberReader


class MemberImport(BaseImport):
    """Importador da tabela member."""

    def __init__(self):
        """Construtor."""
        self.table_name = 'member'
        self.reader = MemberReader()
        super().__init__()

"""."""
from sqlalchemy import create_engine


class MysqlConnection:
    """."""

    def connect(self):
        """."""
        return create_engine(
            'mysql://mydb:mydb@mysqletl_fee_db_1:3306/mydb', echo=False
        )

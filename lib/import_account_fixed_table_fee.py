import pandas as pd
import os
from sqlalchemy import create_engine

engine = create_engine(
      "mysql+pymysql://sylvain:passwd@localhost/db?host=localhost?port=3306")
project_home = os.environ['PROJECT_HOME']

df = pd.read_csv(
    project_home + '/datafiles/account.csv',
    index_col='id',
    names=[
        'id', 'account_id', 'payment_form_id', 'parcel_number',
        'fixed_tax_percentual', 'parcel_tax_percentual', 'fixed_tax_value'
    ],
    delimiter=';'
)

engine = create_engine(
    'mysql+mysqlconnector://mydb:mydb@localhost:3306/mydb', echo=False
)
cnx = engine.raw_connection()
df.to_sql(
    name='account', con=cnx, schema='mydb', if_exists='replace', index=True
)

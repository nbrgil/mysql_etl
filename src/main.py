"""."""
from csv_reader.account_reader import AccountReader

acc = AccountReader()
acc.read()
print(acc.df)

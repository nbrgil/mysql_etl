#!/usr/bin/env bash

echo 'Project home dir: '${PROJECT_HOME}
mysql -u mydb -h mysqletl_fee_db_1 --port 3306 --password="mydb" < ${PROJECT_HOME}/script/clear_tables.sql
echo 'Importing...'
# python ${PROJECT_HOME}/lib/account_import.py && echo '--> account.csv ok'
# python ${PROJECT_HOME}/lib/member_import.py && echo '--> member.csv ok'
# python ${PROJECT_HOME}/lib/payment_method_import.py && echo '--> payment_method.csv ok'
# python ${PROJECT_HOME}/lib/fee_import.py && echo '--> fee.csv ok'


python ${PROJECT_HOME}/src/main.py && echo '--> ok'

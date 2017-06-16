#!/usr/bin/env bash

echo 'Project home dir: '${PROJECT_HOME}
echo 'Importing account...' && (python ${PROJECT_HOME}/lib/import_account.py && echo 'ok')

#!/bin/sh
mysql -u $1 -p $2 $3 < "setup_database.txt";
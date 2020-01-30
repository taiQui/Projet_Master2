#!/bin/sh
echo "[+] First setup database"
mysql -u root -p < "setup_database.txt"
echo "[+] Creation database by django"
echo "		[*] Follow step asked "
cd site_owasp
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser

echo "[+] Database created"

echo "[+] Adding comparison flag tables and adding flag"
mysql -u root -p < "setup_database2.txt"

#!/bin/sh
if [ $? -eq 0 ]
then
  echo $0" username(root) file_with_password_for_username"
  exit
fi
for i in $#
do
  if [ '-h' -eq $i ]
    then
    echo $0" username(root) file_with_password_for_username"
    exit
  fi
done

echo "[+] First setup database"
mysql -u $1 --password=$(cat $2) < setup_database.sql;
mysql -u $1 --password=$(cat $2) sql_injection < setup_database_sql_injection.sql;

echo "[+] Creation database by django"
echo "		[*] Follow step asked "
cd site_owasp
python3 manage.py makemigrations
python3 manage.py migrate
echo "[+] Enter your password (admin)"
python3 manage.py createsuperuser --point=0 --nom=admin
echo "[+] Database created"
cd ../
echo "[+] Adding comparison flag tables and adding flag"
mysql -u $1 --password=$(cat $2) owasp < /home/taiqui/Documents/Fac/M2/PROJET/Projet_Master2/setup_database2.sql;

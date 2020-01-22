echo "[+] Installing python"
sudo apt-get install software-properties-common > /dev/null
sudo add-apt-repository ppa:deadsnakes/ppa > /dev/null
sudo apt-get update > /dev/null
sudo apt-get install python3.6 > /dev/null

echo "[+] Installing Django "
sudo pip3 install Django > /dev/null

echo "[+] Installing Mysql package"
sudo apt-get install python3-dev libmysqlclient-dev > /dev/null
sudo pip3 install mysqlclient > /dev/null

echo "[+] Setup mysql"
echo "	[*] Stopping mysql service"
sudo /etc/init.d/mysql stop > /dev/null
echo "	[*] Changing root password to root"
sudo mysqld_safe --skip-grant-tables &
mysql -u root < setup.txt > /dev/null
echo "	[*] Creation database for SQL challenge"
echo "	[*] Enter 'root' as password"
mysql -u root -p < setup2.txt > /dev/null
echo "	[*] Creating User www-data with password \"flagados_le_sang\""
echo "	[*] Creating database sql_injection with table user and adding some user"
echo "[+] Printing django Version "
python -m django --version
echo"[+] Creating django project on ~/Document/ for each vulnerabilities" 
cd ~/Document
django-admin startproject Injection > /dev/null
django-admin startproject Broken_Authentification > /dev/null
django-admin startproject Sensitive_data_exposure > /dev/null
django-admin startproject XXE > /dev/null
django-admin startproject Broken_access_control > /dev/null
django-admin startproject Security_misconfiguration > /dev/null
django-admin startproject XSS > /dev/null
django-admin startproject Insecure_deserialization > /dev/null
django-admin startproject Components_know_vuln > /dev/null
django-admin startproject Insufficient_logging_monitoring > /dev/null

echo "	[*] Creating Apps for each project"
cd Injection
python3 manage.py startapp Index > /dev/null
python3 manage.py startapp Basic > /dev/null
python3 manage.py startapp Blind_based > /dev/null
python3 manage.py startapp Error_based > /dev/null
cd ../Broken_Authentification
python3 manage.py startapp Index > /dev/null
python3 manage.py startapp admin > /dev/null
cd ../Sensitive_data_exposure
python3 manage.py startapp Index > /dev/null
cd ../XXE
python3 manage.py startapp Index > /dev/null
cd ../Broken_access_control
python3 manage.py startapp Index > /dev/null
cd ../Security_misconfiguration
python3 manage.py startapp Index > /dev/null
cd ../XSS
python3 manage.py startapp Index > /dev/null
cd ../Insecure_deserialization
python3 manage.py startapp Index > /dev/null
python3 manage.py startapp profile > /dev/null
cd ../Components_know_vuln
python3 manage.py startapp Index > /dev/null


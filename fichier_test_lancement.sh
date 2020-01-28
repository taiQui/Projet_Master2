echo "[+] demmarage de mysql"
sudo systemctl start mysql
echo "[+] ok mysql"
# alors machine
# principale              8080
# injection               8081 +
# broken_authentification 8082
# broken acces control    8083
# insecure Insecure_deser 8084 +
# insuf log               8085
# Security_misconfigurati 8086 +
# sensitive data          8087
# using comp vul          8088 +
# xml                     8089
# xss                     8090 

echo "[+] demmarage de toute les vm pour les test"
cd site_owasp/
sudo python3 manage.py runserver 8080 &
echo "[+] ok owasp"
#
# cd ../VM/Injection
# sudo python3 manage.py runserver 8081 &
# echo "[+] ok pour injection"
#
# cd ../VM/CKV
# sudo python3 manage.py runserver 8088 &
# echo "[+] ok pour CKV"
#
# cd ../VM/Insecure_deserialization
# sudo python3 manage.py runserver 8083 &
# echo "[+] ok pour Insecure_deserialization"
#
# cd ../VM/Security_misconfiguration
# sudo python3 manage.py runserver 8084 &
# echo "[+] ok pour Security_misconfiguration"
#
# cd ../VM/XSS
# sudo python3 manage.py runserver 8085
# echo "[+] ok pour XSS"

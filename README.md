# Projet_Master2
Projet universitaire master 2 - UPHF

Requiere :

* python3

  * django : pip3 install django
  * mysql-connector : pip3 install mysql-connector
  * mysqldb : pip3 install MysqlDb
* apt
  * mysql : apt install mysql-client && apt install mysql-server

## Lancement

```bash
# Il faut crée un fichier contenant le password de l'utilisateur de la base de donnée ( root )
chmod +x setup.sh
./setup.sh root file_with_password_in
# Suivre les instructions
[...]
python3 launch.py
# Lance tous les serveurs
firefox localhost:8080 &
# Ouvre firefox sur le site
```



  









# Ressources - Première idées

# Rappel github

**git pull ** avant chaque session de travail ainsi que avant de push
**git add [file] ** pour ajouté les fichiers
**git commit -m "comment"**
**git push**

## Github fonctionnement des branches
**git branch [nomBranche] **  création d'une branches
**git checkout [nomBranche] ** basculement sur une branche
**git push origin [nomBranche] ** push la branche sur github

# Idée
Sensibilisation des 10 failles OWASP
  * Faire des demo style box HTB pour les failles ( possiblement TP de fin)
  * Site internet avec authentification
  * page par failles
  * explication, prevention, demo, se prémunirs

Possibilité de sensibilisation sur ransomware ( creation ransomware )


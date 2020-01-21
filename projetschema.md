# Injection SQL

- **Agents de menace / vecteurs d'attaque** : On peut supposer que presque toutes les sources de données peuvent être un vecteur d'injection comme des variables d'environnement, des paramètres, des services Web externes et internes et tous les types d'utilisateurs. Les failles d'injection se produisent lorsqu'un attaquant veut envoyer des données malveillante à un interpréteur SQL.

- **Faille de sécurité** : les failles d'injection sont très répandues, en particulier dans le code hérité. Les vulnérabilités d'injection se trouvent souvent dans les requêtes SQL, LDAP, XPath ou NoSQL, les commandes du système d'exploitation, les analyseurs XML, les en-têtes SMTP, les langages d'expression ou encore les requêtes ORM. Les scanners et les fuzzers peuvent aider les attaquants à trouver des défauts d'injection.
- **Impacts** : l'injection peut entraîner une perte de données, la corruption ou la divulgation à des parties non autorisées, la perte de responsabilité ou le refus d'accès. L'injection peut parfois conduire à une prise de contrôle complète de l'hôte. L'impact commercial dépend des besoins de l'application et des données.

### L'application est-elle vulnérable?

Une application est vulnérable aux attaques lorsque:

- Les données fournies par l'utilisateur ne sont pas validées ou filtrées par l'application.
- Les requêtes dynamiques ou les appels non paramétrés sans échappement contextuel sont utilisés directement dans l'interpréteur.
- Les données hostiles sont utilisées dans les paramètres de recherche de la cartographie relationnelle objet (ORM) pour extraire des enregistrements sensibles supplémentaires.
- Les données hostiles sont directement utilisées ou concaténées, de sorte que le SQL ou la commande contient à la fois la structure et les données hostiles dans des requêtes dynamiques, des commandes ou des procédures stockées.
- Certaines des injections les plus courantes sont SQL, NoSQL, commande OS, Object Relational Mapping (ORM), LDAP et Expression Language (EL) ou Object Graph Navigation Library (OGNL). Le concept est identique parmi tous les interprètes. L'examen du code source est la meilleure méthode pour détecter si les applications sont vulnérables aux injections, suivi de près par des tests automatisés approfondis de tous les paramètres, en-têtes, URL, cookies, JSON, SOAP et entrées de données XML. Les organisations peuvent inclure des outils de source statique ( [SAST](https://owasp.org/www-community/Source_Code_Analysis_Tools) ) et de test d'application dynamique ( [DAST](https://owasp.org/www-community/Vulnerability_Scanning_Tools) ) dans le pipeline CI / CD pour identifier les failles d'injection nouvellement introduites avant le déploiement en production.

Exemple d'attaque SQL : On imagine un serveur communicants avec sa base SQL se fait attaquer.

- Etape 1 : Le hacker va lancer une requête SQL malveillante sur le serveur (Ex! un SiteWeb)
- Etape 2 : Le serveur va renvoyer la requête SQL malveillante sur la Base de donnée
- Etape 3 : La base de donnée va répondre à la requête SQL malveillante au serveur
- Etape 4 : Le serveur renvoie la réponse de la requêtes SQL malveillante à l'attaquant

Un exemple simple du fonctionnement d'une requête SQL malveillante

IMAGE EXEMPLESQL

 

POUR LE PROJET : faire une attaque avec or '1'='1

OU faire une attaque BLIND BASED 

les deux sont simple a comprendre :)



Pour rentrer plus en profondeur je vais détailler la famille des 5 injections SQL

Attaque 1 : Blind Based

L'injection aveugle SQL est un type d'attaque qui pose des questions vraies ou fausses à la base de données et détermine la réponse en fonction de la réponse des applications

SCHEMA A VENIR

Attaque 2 : Time Based

Presque identique à la première, cependant, la réponse est détermine en fonction du temps de réponse des applications

SCHEMA A VENIR

Attaque 3 : Error Based

Cette méthode profite d'une faiblesse des systèmes de base de données permettant de détourner un message d'erreur généré par la base de données et préalablement volontairement provoquée par l'injection SQL pour lui faire retourner une valeur précise récupérée en base de données

SCHEMA A VENIR

Attaque 4 : Union Based

/



Attaque 5 : Stacked Queries

/



# Broken Authentification

- **Agents de menace / vecteurs d'attaque** : les attaquants ont accès à des centaines de millions de combinaisons de nom d'utilisateur et de mot de passe valides pour le bourrage des informations d'identification, les listes de comptes administratifs par défaut on appelle sa un "dictionnaire". Les attaques de gestion de session sont bien réel, en particulier en ce qui concerne les jetons de session non expirés.
- **Faille de sécurité** : La prévalence de l'authentification rompue est répandue en raison de la conception et de la mise en œuvre de la plupart des contrôles d'identité et d'accès. La gestion de session est le fondement des contrôles d'authentification et d'accès et est présente dans toutes les applications avec état. Les attaquants peuvent détecter une authentification rompue à l'aide de moyens manuels et les exploiter à l'aide d'outils automatisés avec des listes de mots de passe et des attaques par dictionnaire.
- **Impacts** : les attaquants doivent avoir accès à seulement quelques comptes ou à un seul compte administrateur pour compromettre le système. Selon le domaine de l'application, cela peut permettre le blanchiment d'argent, la fraude à la sécurité sociale et le vol d'identité, ou divulguer des informations hautement sensibles protégées par la loi.

------

### L'application est-elle vulnérable?

La confirmation de l'identité, de l'authentification et de la gestion de session de l'utilisateur sont essentielles pour se protéger contre les attaques liées à l'authentification. Il peut y avoir des faiblesses d'authentification si l'application:

- Autorise les attaques automatisées telles que le [bourrage d'informations](https://www2.owasp.org/www-community/attacks/Credental_stuffing) d' [identification](https://www2.owasp.org/www-community/attacks/Credental_stuffing) , où l'attaquant possède une liste de noms d'utilisateur et de mots de passe valides.
- Autorise la force brute ou d'autres attaques automatisées.
- Autorise les mots de passe par défaut, faibles ou bien connus, tels que «Password1» ou «admin / admin».
- Utilise une récupération des informations d'identification faible ou inefficace et des processus de mot de passe oublié, tels que les «réponses basées sur les connaissances», qui ne peuvent pas être sécurisées.
- Utilise du texte brut, des mots de passe chiffrés ou faiblement hachés (voir [A3: Exposition des données sensibles en 2017](https://www2.owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A3-Sensitive_Data_Exposure) ).
- A une authentification multifacteur manquante ou inefficace.
- Expose les ID de session dans l'URL (par exemple, réécriture d'URL).
- Ne fait pas pivoter les ID de session après une connexion réussie.
- N'invalide pas correctement les ID de session. Les sessions utilisateur ou les jetons d'authentification (en particulier les jetons d'authentification unique (SSO)) ne sont pas correctement invalidés pendant la déconnexion ou une période d'inactivité.



Attaque 1 : Attaque par Brute Force

L'attaquant va alors utiliser pour la plus part du temps un outils, ou un script permettant l'utilisation d'un dictionnaire ou non et lancer plusieurs requêtes jusqu'à deviner le mot de passe



IMAGE ExempleBruteForce



Attaque 2 : Vol de cookie

L'attaquant peut, utiliser par exemple une attaque CSRF sur un utilisateur, en volant sont cookie, il peut usurper l'identité de l'utilisateur sur le serveur et ainsi accéder à des informations non autorisée.

IMAGE ExempleVolCookie 





POUR LE PROJET : Attaque ez a mettre en place, un authentif avec un login et mdp faible.

OU un CSRF sa peut être sympat :spy:








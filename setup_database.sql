drop user IF EXISTS 'www-data'@'localhost';

drop database IF EXISTS owasp;

drop database IF EXISTS sql_injection;

create database sql_injection;

create database owasp;

create user 'www-data'@'localhost' identified by 'www-data';

grant all privileges on sql_injection.* to 'www-data'@'localhost';
grant all privileges on owasp.* to 'www-data'@'localhost';

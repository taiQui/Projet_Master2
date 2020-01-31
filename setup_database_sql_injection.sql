create table users (
	id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name varchar(20) NOT NULL,
	pass varchar(200) NOT NULL,
	pseudo varchar(200),
	work varchar(200),
	points int(100) default 0
);

insert into users(name,pass) values ("admin","Fl4g4d0s_f0R_Th3_W1N");
insert into users(name,pass,pseudo) values ("Jean","Coucou","First_flag_here_:N3v3rg1V3YoUup");
insert into users(name,pass,work) values ("Bon","BAITED","H3llo_H4ck3r");
insert into users(name,pass) values ("De","still_baited");
insert into users(name,pass) values ("Bayonne","already_baited");

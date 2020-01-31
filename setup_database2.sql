create index yolo on pages_flag(flag);
create index yolo2 on pages_myuser(nom);

create table flag_flagged (
	id_flag varchar(50) NOT NULL,
	id_user varchar(20) NOT NULL UNIQUE,
	primary key(id_flag,id_user),
	foreign key(id_flag) references pages_flag(flag),
	foreign key(id_user) references pages_myuser(nom)
);


-- PRIMARY KEY(id_flag,id_user)
-- primary key(id_flag,id_user);

insert into pages_flag(flag) values("Fl4g4d0s_f0R_Th3_W1N");
insert into pages_flag(flag) values("N3v3rg1V3YoUup");
insert into pages_flag(flag) values("H3llo_H4ck3r");
insert into pages_flag(flag) values("R1ckR0ll3d");
insert into pages_flag(flag) values("3d5ac4bba54f7e1eae079a97d5f69e36");
insert into pages_flag(flag) values("dfad37d1d67f40b64cbb5d2228d27fbe");
insert into pages_flag(flag) values("20efe9ebfda4cd9322cd5cf7e7c4f46e");
insert into pages_flag(flag) values("85ea8cabbaf63afa6cbf16956c08b397");

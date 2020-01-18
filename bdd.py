#!/bin/env python3
# coding : utf-8
import mysql.connector,string,random,hashlib
MAX_USER = 20

def generate_random_password():
    return ''.join(random.choice(string.ascii_letters+string.digits) for i in range(32))

class DB:

    def __init__(self,user,password,db,host="localhost"):
        self.username = user
        self.password = password
        self.host     = host
        self.dbname = db
        self.possible_user = []
        for i in range(1,MAX_USER):
            self.possible_user.append(i)
        try:
            self.database = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.dbname
            )
            self.cursor = self.database.cursor()
        except mysql.connector.Error as err:
            print("[-] Error while attempting to connect to the database\n{}".format(err))

    def __repr__(self):
        tables = self.getTables()
        pt = "Tables : "
        for table in tables:
            pt+= "-"+table +"\n"+" "*len("Tables : -")
        return "Database : "+self.dbname+"\n"+pt

    def getTables(self):
        self.cursor.execute("show tables;")
        return self.cursor.fetchall()

    def show_table(self):
        tables = self.getTables()
        for table in tables:
            print(table)

    def getUsers(self):
        self.cursor.execute("select * from users;")
        users = self.cursor.fetchall()[1:]
        return users
    def createUser(self):
        users = self.getUsers()
        name = ""
        if len(users) > MAX_USER:
            raise Exception(MAX_USER+" users are reached")
        else:
            number = []
            for user in users:
                number.append(int(user[1][-1]))
            available_user = [u for u in self.possible_user if u not in number][0]
            random_pass = generate_random_password()
            try:
                self.cursor.execute("insert into users(id,name,pass) values(\'"+str(available_user)+"\',\'user"+str(available_user)+"\',\'"+random_pass+"\');")
                self.database.commit()
                print("[+] {} records inserted.".format(self.cursor.rowcount))
                return ("user"+str(available_user),random_pass)
            except mysql.connector.Error as err:
                print("[-] Error while inserting row to the database.\n{}".format(err))
                return (None,None)
    def deleteUser(self,name):
        try:
            self.cursor.execute("delete from users where name=\'"+name+"\'")
            self.database.commit()
            print("[+] {} Row deleted !".format(self.cursor.rowcount))
        except mysql.connector.Error as err:
            print("[-] Error while deleting row to the database.\n{}".format(err))

    def auth(self,username,password):
        cipher = hashlib.md5()
        cipher.update(password.encode())
        try:
            self.cursor.execute("select * from users where name=\'"+username+"\' and pass=\'"+cipher.hexdigest()+"\'")
            r = self.cursor.fetchall()
            return len(r)==1
        except mysql.connector.Error as err:
            print("[-] Error while attempting to execute select statement.\n{}".format(err))

    def getPoints(self,user):
        try:
            self.cursor.execute("select points from users where name=\'"+user+"\'")
            r = self.cursor.fetchall()
            if len(r) < 1:
                return -1
            return r[0][0]
        except mysql.connector.Error as err:
            print("[-] Error while getting point\n{}".format(err))

    def cleanAll(self):
        try:
            users = self.getUsers()
            for user in users:
                self.cursor.execute("delete from users where name=\'"+user[1]+"\'")
                self.database.commit()
                print("[*] {} deleted !".format(user[1]))
            print("[+] Database cleaned !")
        except mysql.connector.Error as err:
            print("[-] Error while cleaning database.\n{}".format(err))

    def addPoint(self,name,point):
        try:
            pt = int(self.getPoints(name))
            self.cursor.execute("update users set points="+str(point+pt)+" where name=\'"+name+"\'")
            self.database.commit()
            print("[+] {} get {} points, he has now {}.".format(name,point,pt+point))
        except mysql.connector.Error as err:
            print("[-] Error while adding point to {}.\n{}".format(name,err))

    def removePoint(self,name,point):
        try:
            pt = int(self.getPoints(name))
            self.cursor.execute("update users set points="+str(pt-point)+" where name=\'"+name+"\'")
            self.database.commit()
            print("[+] {} lose {} points, he has now {}.".format(name,point,pt-point))
        except mysql.connector.Error as err:
            print("[-] Error while removing point to {}.\n{}".format(name,err))

if __name__ == "__main__":
    a = DB("www-data","www-data","projet")
    # a.show_table()
    # print(a.getUsers())
    # b = a.createUser()
    # a.deleteUser("user1")
    # print(a.getPoints("user1"))
    # a.addPoint("user1",10)
    a.removePoint("user1",10)
    # print(a.getPoints("user1"))

    # a.cleanAll()
    # print(b)

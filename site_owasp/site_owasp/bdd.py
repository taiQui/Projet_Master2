#!/bin/env python3
# coding : utf-8


"""
Class to use mysql Database with python3
simple to use
--------------
    database = DB(user="root",password="root",db="YourDatabase",host="localhost")
"""



import mysql.connector,string,random,hashlib
MAX_USER = 20

def generate_random_password():
    return ''.join(random.choice(string.ascii_letters+string.digits) for i in range(32))




class DB:

    def __init__(self,user,password,db,host="localhost"):
        """
            Define DB class
        """
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
        """
            Allow to "print" DB instance
        """
        tables = self.getTables()
        pt = "Tables : "
        for table in tables:
            pt+= "-"+table +"\n"+" "*len("Tables : -")
        return "Database : "+self.dbname+"\n"+pt

    def getTables(self):
        """
            Return All table from the database
        """
        self.cursor.execute("show tables;")
        return self.cursor.fetchall()

    def show_table(self):
        """
            Print all tables
        """
        tables = self.getTables()
        for table in tables:
            print(table)

    def getUsers(self):
        """
            Return All user from Table Users
        """
        self.cursor.execute("select * from users;")
        users = self.cursor.fetchall()[1:]
        return users
    def createUser(self):
        """
            Create User to use application
            Name would be userX with X in range 1 and MAX_USER
            password is generated randomly with lower,upper,digit with 32 length
            Add user to the database and return creds with tuple
        """
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
        """
            Delete user and print how many line has been removed
        """
        try:
            self.cursor.execute("delete from users where name=\'"+str(name)+"\'")
            self.database.commit()
            print("[+] {} Row deleted !".format(self.cursor.rowcount))
        except mysql.connector.Error as err:
            print("[-] Error while deleting row to the database.\n{}".format(err))

    def auth(self,username,password):
        """
            Test if given credential is in database, return True or False
        """
        cipher = hashlib.md5()
        cipher.update(password.encode())
        try:
            self.cursor.execute("select * from users where name=\'"+str(username)+"\' and pass=\'"+cipher.hexdigest()+"\'")
            r = self.cursor.fetchall()
            return len(r)==1
        except mysql.connector.Error as err:
            print("[-] Error while attempting to execute select statement.\n{}".format(err))

    def getPoints(self,user):
        """
            Return point for given user
        """
        try:
            self.cursor.execute("select point from pages_myuser where nom=\'"+str(user)+"\'")
            r = self.cursor.fetchall()
            if len(r) < 1:
                return -1
            return r[0][0]
        except mysql.connector.Error as err:
            print("[-] Error while getting point\n{}".format(err))

    def cleanAll(self):
        """
            Remove all user except admin from the database
        """
        try:
            users = self.getUsers()
            for user in users:
                self.cursor.execute("delete from users where name=\'"+str(user[1])+"\'")
                self.database.commit()
                print("[*] {} deleted !".format(user[1]))
            print("[+] Database cleaned !")
        except mysql.connector.Error as err:
            print("[-] Error while cleaning database.\n{}".format(err))

    def addPoint(self,name,point):
        """
            Add given point to given user
        """
        try:
            pt = int(self.getPoints(name))
            # print("old pt : "+str(pt))
            # print(type(pt))
            self.cursor.execute("update pages_myuser set point="+str(point+pt)+" where nom=\'"+str(name)+"\'")
            self.database.commit()
            print("[+] {} get {} points, he has now {}.".format(name,point,pt+point))
        except mysql.connector.Error as err:
            print("[-] Error while adding point to {}.\n{}".format(name,err))

    def removePoint(self,name,point):
        """
            Remove given point to given user
        """
        try:
            pt = int(self.getPoints(name))
            self.cursor.execute("update users set points="+str(pt-point)+" where nom=\'"+name+"\'")
            self.database.commit()
            print("[+] {} lose {} points, he has now {}.".format(name,point,pt-point))
        except mysql.connector.Error as err:
            print("[-] Error while removing point to {}.\n{}".format(name,err))

    def getUser(self,name):
        try:
            self.cursor.execute("select name from users where name=\'"+name+"\'")
            r = self.cursor.fetchall()
            if len(r) > 0:
                return r
            else:
                return []
        except mysql.connector.Error as err:
            print("[-] Error while getting user")
    def blind_getUser(self,name):
        try:
            self.cursor.execute("select name from users where name=\'"+name+"\'")
            r = self.cursor.fetchall()
            print(r)
            if len(r) > 0:
                return "Right !"
            else:
                return "Wrong !"
        except mysql.connector.Error as err:
            print("[-] Error while getting user")
    def error_getUser(self,name):
        try:
            if ' or ' in name or ' and ' in name or '#' in name or " union " in name :
                return [("Le piratage c'est pas bien, jeune padawan du hacking !",)],None
            self.cursor.execute("select name from users where name=\'"+name+"\'")
            r = self.cursor.fetchall()
            print(r)
            if len(r) > 0:
                return r,None
            else:
                return [],None
        except mysql.connector.Error as err:
            return str(err),"command : select name from users where name=\'"+name+"\'"
            # print("[-] Error while getting user")
    def validFlag(self,flag):
        try:
            self.cursor.execute("select * from pages_flag where flag=\'"+flag+"\'")
            valid = self.cursor.fetchall()
            return len(valid)>0
        except mysql.connector.Error as err:
            return False
    def already_validate(self,flag,user):
        try:
            self.cursor.execute("select * from flag_flagged where id_flag=\'"+str(flag)+"\' and id_user=\'"+str(user)+"\'")
            a = self.cursor.fetchall()
            print("yolo : "+str(a))
            if len(a) > 0:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            return None
    def add_to_flagged(self,flag,user):
        try:
            self.cursor.execute("insert into flag_flagged(id_flag,id_user) values (\'"+str(flag)+"\',\'"+str(user)+"\')")
            self.database.commit()
            return True
        except mysql.connector.Error as err:
            print(err)
            return None

if __name__ == "__main__":
    a = DB("www-data","www-data","sql_injection")
    # a.show_table()
    # print(a.getUsers())
    # b = a.createUser()
    # a.deleteUser("user1")
    # print(a.getPoints("user1"))
    # a.addPoint("user1",10)
    print(a.blind_getUser("admin' and (select left(password,1) from users where name='admin')='d'-- -"))
    # print(a.getPoints("user1"))


    # a.cleanAll()
    # print(b)

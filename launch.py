#!/bin/env python3
# coding : utf-8
from threading import Thread
from multiprocessing import Process
import subprocess,time,os

PORT = ["8080","8081","8084","8086","8088","8090"]
PORT_OPEN = [False,False,False,False,False,False]
PATH = ["site_owasp","VM/Injection","VM/Insecure_deserialization","VM/Security_misconfiguration","VM/CKV","VM/XSS"]
IP = "localhost"

UP = 0
DOWN = 1

# class Launch(Thread):
#     def __init__(self,path,port):
#         Thread.__init__(self)
#         self.path=path
#         self.port = port
#     def run(self):
#         subprocess.run(["python3",self.path+"/manage.py","runserver",self.port],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)


def Launch(path,port):
    subprocess.run(["python3",path+"/manage.py","runserver",port],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)


def Ping():
    global PORT_OPEN,PORT
    continuer = True
    while continuer == True:
        continuer = False
        for port in PORT:
            rep = subprocess.run(["lsof","-i:"+port],stdout=subprocess.PIPE)
            if rep.returncode == DOWN:
                continuer = True
                PORT_OPEN[PORT.index(port)] = False
            elif rep.returncode == UP:
                PORT_OPEN[PORT.index(port)] = True
            time.sleep(0.05)
        if continuer == False:
            break
if __name__ == "__main__":
    process_tab = []
    for index in range(len(PATH)):
        # Launch(PATH[index],PORT[index]).start()
        process_tab.append(Process(target=Launch,args=(PATH[index],PORT[index],)))
        process_tab[-1].start()
    ping = Thread(target=Ping)
    ping.start()
    while ping.isAlive():
        str = "|   "
        for index in range(len(PORT_OPEN)):
            str+= PORT[index]+": "
            str+= "OPEN    |   " if PORT_OPEN[index] == True else "FALSE   |   "
        print(str,end="\r")
        time.sleep(0.05)
    print("\n")
    input("Quit ? [Press any key]")
    for process in process_tab:
        process.terminate()
        time.sleep(0.1)
        process.join()
    os.system('sudo killall -9 python3')

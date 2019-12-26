#!/usr/bin/env python3

import argparse,subprocess,libvirt
from vm import VM,change,waiting

all_port = ["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009"]

def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--action',help="Define action for VM between - Run Servers (RS) - Stop serveur (SS) - Run VM (RV) - Stop VM (SV) ",required=True)
    parser.add_argument('-p','--port',help="Give port",type=int)
    return parser.parse_args()

def parsing2dict(arg):
    parse = dict()
    if args.action.upper() not in ["RS","SS","RV","SV"]:
        raise Exception("Action not found")
    parse['action'] = arg.action
    parse['port'] = arg.port
    return parse
# !!!!!!!!!!!!!!!!!!!!!!
# CHANGER ICI LE PROCESSUS
# !!!!!!!!!!!!!!!!!!!!!!
def getProcess():
    tmp_output = subprocess.run(["ps","aux"],stdout=subprocess.PIPE)
    liste = tmp_output.stdout.decode('utf-8').split('\n')
    liste = liste[:-1]
    for i in range(len(liste)):
        if len(liste[i]) > 0:
            liste[i] = [ s for s in liste[i].split(' ') if s != '']
            liste[i] = liste[i][1:2]+liste[i][10:]
    return [s for s in liste if "manager.py" in s]  ## replace manager.py by name of processus

def getRunnningPort():
    liste = getProcess()
    portrunning = []
    for i in liste:
        if '--port' in i:
            portrunning.append(i[i.index('--port')+1])
        elif '-p' in i:
            portrunning.append(i[i.index('-p')+1])
    print(portrunning)

def killServers(PortListe):
    if type(PortListe) != []:
        raise Exception('Need list not '+str(type(PortListe)))
    for port in PortListe:
        if not port.isdigit():
            raise Exception('Need Number as port')
        killServer(port)

def killServer(port):
    # !!!!!!!!!!!!
    # Adding commnde to kill process
    subprocess.run(["COMMANDE","'kill -9 "+str(port)+"'"])

def LaunchServers(PortListe):
    if type(PortListe) != []:
        raise Exception('Need liste not '+str(type(PortListe)))
    for port in PortListe:
        if not port.isdigit():
            raise Exception('Need number as port')
        LaunchServer(port)

def LaunchServer(port):
    # !!!!!!!!!!!!
    # Adding commnde to launch process
    subprocess.run(["COMMAND","'python3 /path/to/file --port "+str(port)+"'"])

def StopVM():
    VM().execute("stop")
def StartVM():
    VM().execute("start")
    waiter = waiting()
    waiter.start()
    wait = "Waiting for VM |"
    while  w.is_alive():
        print(wait,end="\r")
		wait = change(wait)
		time.sleep(0.2)
    print("[+] Done")

def Execute(args):
    if args['action'] == "RS":
        if args['port'] == None:
            print("You not mentioned port to start web server\nDo you want start all server ? [Y/N]")
            if input().upper() == "Y":
                LaunchServers(all_port)
        else:
            print("[+] Starting server on port "+args['port'])
            LaunchServer(args['port'])
    elif args['action'] == "SS":
        if args['port'] == None:
            print("You not mentioned port to stop web server\nDo you want stop all server ? [Y/N]")
            if input().upper() == "Y":
                killServers(all_port)
        else:
            print("[+] Stoping server on port "+args['port'])
            killServer(args['port'])
    elif args['action'] == "RV":
        StartVM()
    elif args['action'] == "SV":
        StopVM()

if __name__ == "__main__":
    args = parsing2dict(parsing())
    Execute(args)

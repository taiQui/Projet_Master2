import os


for path,dir,files in os.walk('.'):
    for file in files:
        if file.endswith('.pyc'):
            print("[+] "+path+"/"+file+" deleted !")
            os.system('rm '+path+"/"+file)

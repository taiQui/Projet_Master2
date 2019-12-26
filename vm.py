#!/usr/bin/env python3
import libvirt

class waiting(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		while True:
			a = subprocess.run(["ping","VM","-c","1"],stdout=subprocess.PIPE)
			try:
				if int(a.stdout.decode('utf-8').split('packets transmitted, ')[1].split(' received')[0]) == 1 and int(b.stdout.decode('utf-8').split('packets transmitted, ')[1].split(' received')[0]) == 1:
					time.sleep(3)
					break
			except:
				pass

def change(a):
	if "|" in a:
		return "Waiting for VM /"
	if "/" in a:
		return "Waiting for VM —"
	if "—" in a:
		return "Waiting for VM \\"
	if "\\" in a:
		return "Waiting for VM |"

class VM():
    def __init__(self):
        self.name = "NAME OF VM"
        self.machine = libvirt.open('qemu:///system').lookupByName(self.name)

    def start(self):
        print(Color.red+"Starting the virtual machine "+self.name+Color.default)
        self.machine.create()

    def stop(self):
        print(Color.red+"Stoping the virtual machine "+self.name+Color.default)
        self.machine.destroy()

    def resume(self):
        print(Color.red+"Resume the virtual machine "+self.name+Color.default)
        self.machine.resume()

    def suspend(self):
        print(Color.red+"Suspend the virtual machine "+self.name+Color.default)
        self.machine.suspend()

    def info(self):
        print(Color.red+"Printing info for "+self.name+Color.default)
        state,maxmem,mem,cpus,cput = self.machine.info()
        print("   The state is "+str(state))
        print("   The max memory is "+str(maxmem))
        print("   The memory is "+str(mem))
        print("   The number of cpus is "+str(cpus))
        print("   The cpi time is "+str(cput))

    def execute(self,action):
        if action == "start":
            try:
                self.start()
            except:
                print("Probably trying to start "+self.name+" when alreary active")
        elif action == "stop":
            try:
                self.stop()
            except:
                print("Probably trying to stop "+self.name+" when already stopped")
        elif action == "resume":
            try:
                self.resume()
            except:
                print("Probably trying to resume "+self.name+" when not paused")
        elif action == "suspend":
            try:
                self.suspend()
            except:
                print("Probably trying to suspend "+self.name+" when already suspended")
        elif action == "info":
            self.info()
        else:
            print("Undefined action !")

import subprocess as sub
import tkinter as tk
import os, time, threading, sys, platform

#Important/global variables
global scriptNames, scriptObjs, dir, osName, key
scriptNames=["spam", "message", "internet", "typer", "lucky"]
osName=platform.system()
key=False
#Get proper dir path
if platform.system()=="Windows":
	dir=os.environ["USERPROFILE"]+"\\.Network\\"
else:
	dir=os.getcwd()+"/.Network/"

#Main
def main():
	global t1, t2
	t1=myThread(window)
	t2=myThread(checkFolder)

	t1.start()
	t2.start()

class myThread(threading.Thread):
	def __init__(self, func):
		threading.Thread.__init__(self)
		self.func=func

	def run(self):
		self.func()

def window():
	global scriptObjs, dir
	root=tk.Tk()
	root.title("Virus Detected!")

	#Create list of button objects
	scriptObjs=[tk.Button(root, text=name) for name in scriptNames]

	#Splat a label before the buttons!
	intro=tk.Label(root, text="Uh oh! Looks like you have a virus!")
	intro2=tk.Label(root, text="Select one of the following options:")

	intro.grid(row=0, column=0, columnspan=len(scriptObjs), pady=(10, 0))
	intro2.grid(row=1, column=0, columnspan=len(scriptObjs), pady=(0, 10))

	#Smush those butts into a grid!
	for i in range(len(scriptObjs)):
		scriptObjs[i].grid(row=2, column=i, pady=(0, 10))

	#Have to bind each button individualy cuz tkinter is silly
	#(I think it evaluates the function after press?)
	scriptObjs[0].bind("<Button-1>", lambda x:run(dir, scriptNames[0], ".vbs"))
	scriptObjs[1].bind("<Button-1>", lambda x:run(dir, scriptNames[1], ".vbs"))
	scriptObjs[2].bind("<Button-1>", lambda x:run(dir, scriptNames[2], ".vbs"))
	scriptObjs[3].bind("<Button-1>", lambda x:run(dir, scriptNames[3], ".vbs"))
	scriptObjs[4].bind("<Button-1>", lambda x:run(dir, scriptNames[4], ".vbs"))

	root.protocol("WM_DELETE_WINDOW", root.quit)
	#root.protocol("WM_DELETE_WINDOW", doNothing)
	root.mainloop()

def run(path, name, extension):
	global key
	name+=extension

	#Unlocking
	print("I'm gonna start '{}' in path {}!".format(name, path))
	key=True
	if osName=="Windows":
		setMode(path, "grant")
	else:
		setMode(path, 493)

	#Executing script
	try:
		sub.Popen(["start", "{}{}".format(path, name)], shell=True)
	except FileNotFoundError:
		errorPopup("FileNotFoundError\n{}{}".format(path, name))
	except:
		errorPopup("UnknownError")

	#Locking
	if osName=="Windows":
		setMode(path, "deny")
	else:
		setMode(path, 0)
	key=False

def errorPopup(errorName):
	root=tk.Tk()
	root.title("Error")
	label=tk.Label(root, text="There was an error while running the program:")
	error=tk.Label(root, text=errorName)
	label.grid(row=0, column=0, padx=10, pady=10)
	error.grid(row=1, column=0, pady=(0, 10))

def stdPopup(title):
	root=tk.Tk()
	root.title(title)

def setMode(path, newMode):
	try:
		os.chmod(path, newMode)
	except:
		print(end="\t")
		sub.Popen(["Icacls", path, "/{}".format(newMode), "%USERNAME%:f"], shell=True, stdout=None)

def doNothing():
	print("Not doing anything lol!")

def checkFolder():
	global dir, key, t1, osName
	print("Starting folder guard!")
	try:
		curMod=os.stat(dir)[0]
	except FileNotFoundError:
		sub.Popen(["python", "writeScripts.py"], shell=True)
		print("I couldn't find the 'Network' folder so i re-wrote it!")
		time.sleep(3)
	except PermissionError:
		print("Permission to set curMod denied!")
		print("Probably on Windows, so I'm gonna try this...")
		if os.path.isdir(dir):
			results=sub.Popen(["Icacls", "{}".format(dir)], shell=True, stdout=sub.PIPE)
			permissions=(results.stdout.read()).decode(encoding="UTF-8").split('\n')
			curMod=permissions[0]

	#Test for access
	while t1.is_alive() and os.path.isdir(dir):
		results=sub.Popen(["Icacls", "{}".format(dir)], shell=True, stdout=sub.PIPE)
		nowCheck=(results.stdout.read()).decode(encoding="UTF-8").split('\n')
		nowCheck=nowCheck[0]
		try:
			time.sleep(1)
			print("\tcurMod: {}\n\tcmd: {}".format(curMod, nowCheck))
			if key and curMod!=nowCheck:
				print("Folder accessed internally!")
				time.sleep(1)
			elif not key and curMod!=nowCheck:
				print("Folder accessed externally!")
				print("Cleaning folder!")
				try:
					sub.Popen(["rm", "-rf", "{}".format(dir)], shell=True)
				except:
					print("Something went wrong!")
				break
			else:
				pass
				#print("Folder locked!")
		except:
			pass
	print("Done guarding folder!")





if __name__=="__main__":
	main()

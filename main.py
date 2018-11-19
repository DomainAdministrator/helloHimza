import tkinter as tk
import subprocess as sub
import os, time, sys, threading, platform

#Global variables
global quit, dir
quit=False
if platform.system()=="Windows":
	dir=os.environ["USERPROFILE"]+"\\Network\\"
else:
	dir=os.getcwd()+"/"

#Main()
def main():
	global quit
	mainRoot()
	'''
	while True:
		mainRoot()
		if quit:
			break
	'''


def mainRoot():
	#Root Stuff
	root=tk.Tk()
	root.title("Virus Detected")

	#Labels & Buttons
	label=tk.Label(root, text="A virus has been found on this computer!\nTo avoid \
potentially fatal damage, select one of the options below:")
	diagnose=tk.Button(root, text="Diagnose", command=root.destroy)
	close=tk.Button(root, text="Close", command=root.destroy)
	spam=tk.Button(root, text="Spam")
	message=tk.Button(root, text="Message")
	internet=tk.Button(root, text="Internet")
	typer=tk.Button(root, text="Typer")
	password=tk.Entry(root, width=50)

	#Binding buttons to functions
	spam.bind("<Button-1>", lambda event:executeVBS(event, "spam"))
	message.bind("<Button-1>", lambda event:executeVBS(event, "message"))
	internet.bind("<Button-1>", lambda event:executeVBS(event, "internet"))
	typer.bind("<Button-1>", lambda event:executeVBS(event, "typer"))
	#Main Loop & gridding
		#row 0
	label.grid(row=0, columnspan=10, padx=10, pady=10)

		#row 1
	diagnose.grid(row=1, column=0, pady=(0, 10))
	close.grid(row=1, column=1, pady=(0, 10))
	spam.grid(row=1, column=2, pady=(0, 10))
	message.grid(row=1, column=3, pady=(0, 10))
	typer.grid(row=1, column=4, pady=(0, 10))
	internet.grid(row=1, column=5, pady=(0, 10))

		#row 2
	password.grid(row=2, pady=(0, 10), columnspan=10)
	root.protocol("WM_DELETE_WINDOW", doNotClose)
	root.mainloop()



def doNotClose():
	pass

def didntWork(errorName):
	root=tk.Tk()
	root.title("Didn't Work!")
	tk.Label(root, text="Oops! This went wrong:").pack()
	tk.Label(root, text="{}".format(errorName)).pack()

def executeVBS(event, scriptName):
	global dir
	command=dir+scriptName+".vbs"
	print(command)
	print("Executing '{}' x".format(scriptName))
	try:
		x=sub.call([command], shell=True)
		if x!=0:
			raise Exception()
	except Exception:
		didntWork("Shell Error")
	except KeyboardInterrupt:
		didntWork("KeyboardInterrupt")
	except FileNotFoundError:
		didntWork("FileNotFoundError")
	except OSError:
		didntWork("OSError")
	except:
		didntWork("Unknown Error")


if __name__=="__main__":
	main()

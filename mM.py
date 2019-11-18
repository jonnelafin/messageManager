#Made by Jonnelafin, more info at jonnelafin.github.io
#Direct contact: elias.eskelinen@protonmail.com

extraout = False
noout = False

def err(msg):
	print("ERROR: " + msg)
def succ(msg):
	if extraout == False or noout == True:
		return
	print("SUCCESS: " + msg)
def readMessages(file = "messages.mMR"):
	out = ""
	try:
		with open(file, "r+") as f:
			out = f.read()
			succ("Message record file read!")
	except Exception as e:
		err("There was problem reading the message record file:")
		err(str(e))
	return out

#Main
def interface():
	readMessages()

#Execute the main function
interface()

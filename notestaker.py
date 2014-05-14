#!/usr/bin/env python
#this is script that stores notes for the user
#just something i thought that it might be cool to make
#Programmer Matthew Deig
#I might to add a way to del enrties in the notes
import sys
import os

if os.name == "nt":
	homeDir = "C:" + os.environ["HOMEPATH"] + os.sep + ".notes" + os.sep
	fileDir = homeDir + "notes"
else:
	homeDir = os.environ["HOME"] + os.sep + ".notes"+ os.sep
	fileDir = homeDir + "notes"
	
def writeNote(NoteString):
	if os.access(fileDir, os.F_OK):
		file = open(fileDir, "a")
		file.write("\n"+NoteString)
		file.close()
	else:
		file = open(fileDir, "w")
		file.write(NoteString)
		file.close()
	
	
def readNotes():
	if os.access(fileDir, os.F_OK):
		x = 0
		linecounter = 1
		file = open(fileDir, "r")
		filestring = ""
		while x == 0:
			tempstring = file.readline()
			if tempstring == "":
				x = 1
			else:
				if filestring == "":
					filestring = (str)(linecounter) + ". " + tempstring
				else:
					filestring = filestring + (str)(linecounter) + ". " + tempstring
				linecounter = linecounter + 1
		file.close()
	else:
		filestring = "File has not been made use -w to make the file"
	return filestring

def deleteNotes(deletelines):
	mulilinedelete = 0
	startline = 0
	endline = 0
	filestring = ""
	newfilestring = []
	deletelines = deletelines.split("-")
	
	if len(deletelines) > 1:
		mulilinedelete = 1
		startline = int(deletelines[0]) - 1
		endline = int(deletelines[1]) - 1
	else:
		startline = int(deletelines[0]) - 1
	
	if os.access(fileDir, os.F_OK):
		file = open(fileDir, "r")
		filestring = file.read()
		file.close()
		
		filestring = filestring.split("\n")
		if mulilinedelete == 0:
			del filestring[startline]
		elif mulilinedelete == 1:
			x = startline
			while(x <= endline):
				del filestring[startline]
				x = x + 1
		
		#put the new lines pack
		x=0
		for y in filestring:
			x+=1
		
		for y in filestring:
			newfilestring.append(y)
			if x > 1:
				newfilestring.append("\n")
			x-=1

		file = open(fileDir, "w")
		file.writelines(newfilestring)
		file.close()		
	else:
		filestring = "File has not been made use -w to make the file"
	

if __name__ == "__main__":
	argpos = 0
	lengthofargs = 0
	writemode = 0
	readmode = 0
	helpmode = 0
	deletemode = 0
	deletearg = ""
	notestring = ""
	if not os.access(homeDir, os.F_OK):
		os.mkdir(homeDir)
	for args in sys.argv:
		if args == "-w":
			for args in sys.argv:
				lengthofargs += 1
			pos = argpos + 1
			while( pos < lengthofargs):
				if(pos == "-r" or pos == "--help"):
					break
				elif(pos != "-r" or pos != "--help" or pos != "-w"):
					notestring = notestring + sys.argv[pos] + " "
				pos += 1
			writemode = 1
		elif args == "-r":
			readmode = 1
		elif args == "--help":
			helpmode = 1
		elif args == "-d":
			pos = argpos + 1
			if sys.argv[pos] != None:
				deletearg = sys.argv[pos]
				deletemode = 1
		argpos+=1
		
	if writemode == 1:
		writeNote(notestring)
	elif readmode == 1:
		print(readNotes())
	elif helpmode == 1:
		print("You need to use -w to write a note")
		print("-r for reading the notes for you")
		print("If this is the first time then use -w")
		print("to delete lines -d line number like -d 1 or -d 1-5 to delete lines 1 through 5")
	elif deletemode == 1:
		deleteNotes(deletearg)
	elif helpmode == 0 and writemode == 0 and readmode == 0 and deletemode == 0:
		print("You need to use -w to write a note")
		print("-r for reading the notes for you")
		print("If this is the first time then use -w")
		print("to delete lines -d line number like -d 1 or -d 1-5 to delete lines 1 through 5")

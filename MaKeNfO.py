import subprocess
import datetime
import os
import getpass

from datetime import datetime

from bs4 import BeautifulSoup

i = 0
dcount = 0
Tcount = 0
Dacount = 1
Scount = 0
NoFil3S = 0
Os = 1
DeeZT1m35 = [0, 0, 0]
ThiSizƎ = 0
TrL1s7 = ""
Ar7is7 = ""
gen = ""

NF0M = ""

WhoOoP5 = False

L457 = ""
M3 = "#"

###Check for 10..
#Check level, EncodE

a = 0

def Woah(h3r3):
	global NoFil3S, TrL1s7, DeeZT1m35
	global L457, M3

	m3 = False

	NfO = ""
	NF0M = ""

	#print(L457)

	for item in os.listdir(h3r3):
		item_path = os.path.join(h3r3, item)

		if os.path.isdir(item_path):
			WhoOoP5 = True

			NfO = fix(NfO, item_path)

			NF0M += NfO.split("Ripped by............:")[0] + "Playing Time.........:" + NfO.split("Playing Time.........:")[1].split("---------------------------------------------------------------------\nIf you like it")[0] + "\n"

			m3 = True

			open((os.path.join(h3r3, ".nfo")), "w").write(NfO.replace("x.X.x", L457).replace("Y.y.Y 😊", M3).replace("HeaD", padMe(h3r3.split("/")[len(h3r3.split("/")) - 1].split(" [")[0])).replace("TR_lis7", f1xMƎ(TrL1s7)).replace("DSotM", IgetThe()).replace("BiG", str(round(ThiSizƎ, 2)) + " MiB"))

			if not m3 and WhoOoP5: 
				NfO = ""
				TrL1s7 = ""
				DeeZT1m35 = [0, 0, 0]

	if m3:
		open(os.path.join(h3r3, h3r3.split("/")[len(h3r3.split("/")) - 1] + ".nfo"), "w").write(NF0M + "---------------------------------------------------------------------\nIf you like it" + NfO.split("---------------------------------------------------------------------\nIf you like it")[1])

	if not m3: open(os.path.join(h3r3, h3r3.split("/")[len(h3r3.split("/")) - 1] + ".nfo"), "w").write(fix(NfO, h3r3))

def fix(NfO, h3r3):
	global NoFil3S, dcount, Tcount, Dacount, Scount, DeeZT1m35, ThiSizƎ, TrL1s7

	NFo = [[[td.get_text(strip=True) for td in tr.find_all('td')] for tr in table.find_all('tr') ] for table in BeautifulSoup(subprocess.run(['mediainfo', h3r3, "--Output=HTML"], capture_output=True, text=True).stdout, 'html.parser').find_all('table')]

	NoFil3S = len([name for name in os.listdir(h3r3) if os.path.isfile(os.path.join(h3r3, name))]) - 2
	howManY()
	NfO = gE7(NfO, h3r3, NFo)

	##print(NfO)

	open(os.path.join(os.path.join(os.path.join("/home/", getpass.getuser()), ".configs/TemPla7Ǝ.nfo")), "r").read()

	dcount = 0
	Tcount = 0
	Dacount = 1
	Scount = 0
	DeeZT1m35 = [0, 0, 0]
	ThiSizƎ = 0
	TrL1s7 = ""

	return NfO.replace("x.X.x", L457).replace("Y.y.Y 😊", M3).replace("s\n   \n", "s\n")

def gE7(nF0, h3r3, NFo):
	global TrL1s7, Ar7is7, gen

	NF0 = open(os.path.join(os.path.join(os.path.join("/home/", getpass.getuser()), ".configs/TemPla7Ǝ.nfo")), "r").read()

	for x in NFo:
		for y in x:
			for z in y:
				if "/cover" in z or ".nfo" in z:
					TrL1s7 = TrL1s7.replace("AAA-", Ar7is7 + " - ")
					##print(DeeZT1m35)
					NF0 = NF0.replace("x.X.x", L457).replace("Y.y.Y 😊", M3).replace("HeaD", padMe(h3r3.split("/")[len(h3r3.split("/")) - 1].split(" [")[0])).replace("TR_lis7", f1xMƎ(TrL1s7)).replace("DSotM", IgetThe()).replace("BiG", str(round(ThiSizƎ, 2)) + " MiB").replace("Geᴎ", gen)
					return NF0
				NF0 = foREPlac3(y, NF0)
			#if "Complete name :" in y: #print("\n" + str(y))
			#else: #print(str(y))

			##### Add setup file infront so it's automatic

def foREPlac3(b, nfO):
	global TrL1s7, Ar7is7, dcount, Tcount, Dacount, ThiSizƎ, Scount, Os

	#check string lengths, " " "[". splikt on \n len.
	#One before las "/" " - ". ##
	#space check homie.. mod add :.dcoun Os 10 OS new Os nuke on - Stop on 10 < oN If can devided by 10 for o, GO ON ELSE STOP..

	match b[0]:
		case "Album :":nfO = nfO.replace("TiT", b[1])
		case "Track name :": 
			if(Tcount == 1):
				##print(Os)
				if (Os > 1.5):
					if(len(str(NoFil3S)) > len(str(Dacount))):
						for x in range(len(str(NoFil3S)) - len(str(Dacount))):
							#print(len(str(NoFil3S)) - len(str(Dacount)))

							#print("No: " + str(len(str(NoFil3S))))
							#print("Da: " + str(len(str(Dacount))))
							TrL1s7 += "0"
						TrL1s7 += str(Dacount) + ". AAA-" +b[1]

					if(len(str(NoFil3S)) == len(str(Dacount))): TrL1s7 += str(Dacount) + ". AAA-" +b[1]
				else:
					TrL1s7 += str(Dacount) + ". AAA-" +b[1]
				Dacount += 1
				Tcount = 0
			else:
				Tcount += 1
		case "Duration :": 
			if(dcount == 3):
				TrL1s7 += " .x." + b[1] + "\n   "
				dcount = 0
				if "h" in b[1]:
					DeeZT1m35[2] += int(b[1].split(" h ")[0]) ### Fix other " mi"
					##print("H: " + b[1].split(" h ")[0])
				if "min" in b[1]:
					if "h" in b[1]:
						DeeZT1m35[0] += int(b[1].split(" min ")[0].split("h ")[1].split(" min")[0])
						##print("Min h: " + b[1].split(" min ")[0].split("h ")[1])
					else:
						DeeZT1m35[0] += int(b[1].split(" min ")[0])
						##print("Min: " + b[1].split(" min ")[0])
				if "s" in b[1]:
					if "min" in b[1]:
						DeeZT1m35[1] += int(b[1].split(" min ")[1].split(" s")[0])
						##print("Sec m: " + b[1].split(" min ")[1])
					else:
						DeeZT1m35[1] += int(b[1].split(" min ")[0].split(" s")[0])
						##print("Sec: " + b[1].split(" min ")[0])
			else:
				dcount += 1
		case "File size :": 
			if (Scount == 1):
				ThiSizƎ += float(b[1].split(" ")[0])
				Scount = 0
			else:
				Scount += 1
		case "Recorded date :": nfO = nfO.replace("y34r", b[1])
		case "Format/Info :": nfO = nfO.replace("C0d.", b[1])
		case "Format :": nfO = nfO.replace(".3Ɔ", " (" + b[1] + ")")
		case "Writing application :": nfO = nfO.replace("V3Rs", b[1])
		case "Compression mode :": nfO = nfO.replace("Qu4L", b[1])
		case "Channel(s) :": nfO = nfO.replace("Ch.", b[1])
		case "Sampling rate :": nfO = nfO.replace(".an", " | " + b[1])
		case "Bit depth :": nfO = nfO.replace(".ɔ3", " | " + b[1])
		case "Performer :": nfO = nfO.replace("4R7", b[1])

	if(len(b) > 1 and "1. " in b[1]):
		geez = b[1].split(" - ")[0]
		Ar7is7 = geez.split("/")[len(geez.split("/")) - 1]
		nfO = nfO.replace("4R7", Ar7is7)

	nfO = nfO.replace("D*", datetime.today().strftime('%Y-%m-%d'))
	nfO = nfO.replace("RiiP", "TRiPPERS")

	return nfO

def howManY():
	global NoFil3S, Os

	NoFil3SN = NoFil3S

	while (NoFil3SN > 1):
		Os *= 10
		NoFil3SN /= 10
		##print(Os)
		##print(NoFil3S)

	if Os != 10 and Os != 1: Os //= 10

def IgetThe():
	global DeeZT1m35

	if DeeZT1m35[1] > 60: 
		DeeZT1m35[0] += DeeZT1m35[1] // 60
		DeeZT1m35[1] %= 60
	if DeeZT1m35[0] > 60: 
		DeeZT1m35[2] += DeeZT1m35[0] // 60
		DeeZT1m35[0] %= 60

	if DeeZT1m35[2] > 0: return str(DeeZT1m35[2]) + " h " + str(DeeZT1m35[0]) + " min " + str(DeeZT1m35[1]) + " sec"
	if DeeZT1m35[0] > 0: return str(DeeZT1m35[0]) + " min " + str(DeeZT1m35[1]) + " sec"
	else: return str(DeeZT1m35[1]) + " sec"

def f1xMƎ(TrL1s7):
	Tr4L1s7 = ""
	oN3 = 0
	s = " "

	for x in TrL1s7.split("\n"):
		if len(x) < 63:
			for y in range(63 - len(x)):
				s += " "
		if oN3 == 0:
			oN3 += 1
			Tr4L1s7 += x.replace(".x.", s[:-4]) + "\n"
		else: 
			Tr4L1s7 += x.replace(".x.", s) + "\n"

		s = ""

	return Tr4L1s7

def padMe(what):
	are = ""

	for x in range((69 - len(what))//2): are += " "

	return are[:-4] + what

def firS7 (a):
	global L457, M3

	if os.path.isfile(os.path.join(os.path.join(os.path.join("/home/", getpass.getuser()), ".configs/SiG.nfo"))):
		a = 1
		L457 = open(os.path.join(os.path.join(os.path.join("/home/", getpass.getuser()), ".configs/SiG.nfo")), "r").read()[:-1]
	else:
		print("Set Signature in: " + os.path.join(os.path.join(os.path.join("/home/", getpass.getuser()), ".configs/SiG.nfo")) + " <--- In this file 😊 .")

	if os.path.isfile(os.path.join(os.path.join(os.path.join("/home/", getpass.getuser()), ".configs/Me.nfo"))):
		a = 1
		M3 = open(os.path.join(os.path.join(os.path.join("/home/", getpass.getuser()), ".configs/Me.nfo")), "r").read()[:-1]
	else:
		print("Enter last message ❤️ in: " + os.path.join(os.path.join(os.path.join("/home/", getpass.getuser()), ".configs/Me.nfo"))+ " <-- File.")

	return a

if firS7(a) == 1:

	h3r3 = input("Enter Music Directory | File 🙂: ")

	gen = input("Enter Genre 🙂: ")

	Woah(h3r3)
import os
from zipfile import ZipInfo, ZipFile
from time import time
import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
  
def brute(zipf,passf):
	new_pass = False
	zipf = ZipFile(zipf)
	time_now = time()
	try:
		new_pass = zipf.extractall("ex",pwd=passf)
		time_final = time()-time_now
		print(bcolors.OKBLUE+"Password found : "+bcolors.OKGREEN+f"{passf.decode('utf-8')}"+bcolors.OKBLUE +f"	in {time_final} seconds"+bcolors.ENDC)
		new_pass = True
		return new_pass

	except Exception:
		pass

def main():
	parser = argparse.ArgumentParser(description = "Bruteforce zipfile",usage="python3 zipt_brute.py -z zipfile -p passfile")
	parser.add_argument("-z","--zipfile",metavar="", required=True,help="input the zip file")
	parser.add_argument("-p","--passfile",metavar="", required=True,help="input password file")

	args = parser.parse_args()
	zipf = args.zipfile
	passf = args.passfile
	if (zipf == None or passf == None):
		print(parser.usage)
		exit(0)
	else:
		try:
			
			zipfile_ = ZipFile(zipf)
		except FileNotFoundError as nof:
			print(bcolors.WARNING+"File does not exist"+bcolors.ENDC)
			exit()
		except zipfile_.BadZipFile:
			print(bcolors.WARNING+"[!] File corrupted... Try again"+bcolors.ENDC)
			exit(0)

	txt_file = open(passf, "rb")
	for line in txt_file:
		line =line.strip()
		new_pass=brute(zipf,line)
		if new_pass == True:
			break
	if new_pass == None:
		print(bcolors.FAIL+"[!] Password not found ..."+bcolors.ENDC)


if __name__ == '__main__':
	main()
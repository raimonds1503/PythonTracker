import time
import os
import sys, getopt
from ftplib import FTP

def main(argv):
	files = []
	mtime = None
	refreshRate = 20
	username = None
	password = None
	host = None
	try:
		opts, args = getopt.getopt(argv, "he:f:r:u:p:d:", ["executable=", "file=", "folder=", "rate=", "username=", "password=", "dns="])
	except getopt.GetoptError:
		print "python track.py -e path"
		sys.exit(2)

	for opt, args in opts:
		if opt in ("-r", "rate="):
			refreshRate = args

		if opt in ("-d", "dns="):
			host = args

		if opt in ("-u", "username="):
			username = args

		if opt in ("-p", "password="):
			password = args

		if 	opt in ("-e", "--executable", "--file"):
			files.append(args)
		elif opt == "-h":
			print "To track folder python track.py -f path \n For tracking file python track.py -e path \n Add -r seconds parameter to set how often the check is made."
			sys.exit(2)
		elif opt in ("-f", "--folder"):
			print "folders not supported yet"
			sys.exit(2)

	if  not files:
		print "Please provide files to be tracked! python track.py -h for help."
		sys.exit(2)

	if not host or not username or not password:
		print "Please provide us with host information. -h for help."
		sys.exit(2)

	print "Connecting to FTP"	
	ftp = FTP('atverts.lv')
	print "Logging into FTP"
	ftp.login('rz', 'skudra')
	ftp.cwd('public_html')
	print "Testing connection"
	ftp.dir()

	print "listening for files ", str(files)
	print "Refresh rate", refreshRate, " seconds"

	while True:
		try:
			print "Checking for changes..."
			if os.stat(files[0]).st_mtime != mtime:
				print "Changes made! Uploading to FTP"
				ftp.storbinary("STOR " + files[0], open(files[0], 'rb'))
				mtime = os.stat(files[0]).st_mtime
			time.sleep(float(refreshRate))
		except (KeyboardInterrupt, SystemExit):
			if ftp:
				print "Closing connection..."
				ftp.quit()
			print "Goodbye (:"
			sys.exit(2)

if __name__ == "__main__":
	main(sys.argv[1:])
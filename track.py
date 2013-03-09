import time
import os
import sys, getopt

def main(argv):
	files = []
	mtime = None
	refreshRate = 20
	try:
		opts, args = getopt.getopt(argv, "he:f:r:", ["executable=", "file=", "folder=", "rate="])
	except getopt.GetoptError:
		print "python track.py -e path"
		sys.exit(2)

	for opt, args in opts:
		if opt in ("-r", "rate="):
			refreshRate = args

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

	print "listening for files ", str(files)
	print "Refresh rate", refreshRate, " seconds"

	while True:
		try:
			print "Checking for changes..."
			if os.stat(files[0]).st_mtime != mtime:
				print "Changes made!"
				mtime = os.stat(files[0]).st_mtime
			time.sleep(refreshRate)
		except (KeyboardInterrupt, SystemExit):
			print "Goodbye (:"
			sys.exit(2)

if __name__ == "__main__":
	main(sys.argv[1:])
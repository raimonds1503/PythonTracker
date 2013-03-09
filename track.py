import time
import sys, getopt

def main(argv):
	files = []
	try:
		opts, args = getopt.getopt(argv, "he:f:", ["executable=", "file=", "folder="])
	except getopt.GetoptError:
		print "python track.py -e path"
		sys.exit(2)

	for opt, args in opts:
		if 	opt in ("-e", "--executable", "--file"):
			files.append(args)
		elif opt == "-h":
			print "To track folder python track.py -f path \n For tracking file python track.py -e path."
			sys.exit(2)
		else:
			print "folders not supported yet"
			sys.exit(2)

	if  not files:
		print "Please provide files to be tracked! python track.py -h for help."
		sys.exit(2)

	print "listening for files ", str(files) 

	while True:
		try:
			print "Checking for changes..."
			time.sleep(2)
		except (KeyboardInterrupt, SystemExit):
			print "Goodbye (:"
			sys.exit(2)

if __name__ == "__main__":
	main(sys.argv[1:])
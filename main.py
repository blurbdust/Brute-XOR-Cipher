import sys, getopt, itertools, requests
from timeit import default_timer as timer

start = timer()
charset = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
filename = ""

def main(argv):
	help_message = "main.py -i <input filename>"
	try:
		opts, args = getopt.getopt(argv,"h:i:n:",["input=", "num="])
	except getopt.GetoptError:
		print help
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print help_message
			sys.exit()
		elif opt in ("-i", "--input"):
			filename = arg

	global charset
	given_file = open(filename, "rb")
	given_string = given_file.read()
	count = 0

	for attempt in bruteforce(charset, 10):
		if (count % 100000) == 0:
			print "Still trying... On " + attempt 
		potential = str_xor(given_string, attempt)		
		if "iasg{" not in potential:
			#Waste a cycle
			count += 1
		else:
			print "Key: " + attempt
			print potential
			sys.exit(2)

def bruteforce(charset, maxlength):
	return (''.join(candidate)
		for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
		for i in range(1, maxlength + 1)))

def str_xor(s1, s2):
	return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/python
import sys, getopt
import random
import os

"""
	author - Akash
	Program - Rotation of a sorted list.
"""

def rotation(N,r, inputdir, outputdir):
	filelist = os.listdir(inputdir)
	count = 1
	output = open(outputdir + 'rotated_list.txt', 'w') 

	# read file from the N-r to N and write it to the file.
	print '\nInput files :'
	for file in filelist:
		print file
		print '\n'
		with open(inputdir + file) as lines:
			for line in lines:
				if(count > N-r and count <= N):
					number = line.strip()
					if number:
						output.writelines(str(number) + '\n')
				count += 1
     
    # read file from 0 to N-r and write to file        		
	count = 1
	for file in filelist:
		with open(inputdir + file) as lines:
			for line in lines:
				if(count <= N-r):
					number = line.strip()
					if number:
						output.writelines(str(number) + '\n')
				count += 1

def main(argv):

	r = 0
	N = 0
	inputdir = ''
	outputdir = ''

	# parse arguments 
	try :
		opts, args = getopt.getopt(argv,"hn:r:i:o:",["enumber=","rnumber=","ifile","ofile"])
	except getopt.GetoptError:
		print 'rotate_sorted_list.py -n <number of elements> -r <number of rotations - random if not defined> -i <input file dir> -o <output  file dir>'
		sys.exit(1)
	for opt, arg in opts:
		if opt == '-h':
			print 'rotate_sorted_list.py -n <number of elements> -r <number of rotations - random if not defined> -i <input file dir> -o <output file dir>'
			sys.exit()
		elif opt in ("-n", "--nelement"):
			N = int(arg)
		elif opt in ("-r", "--nrotation"):
			r = int(arg)
		elif opt in ("-i", "--idir"):
			inputdir = arg
		elif opt in ("-o", "--odir"):
			outputdir = arg

	# assign a random value to the rotation facor if r = 0
	if N == 0:
		print '\nInvalid value of N. Exiting...!'
		sys.exit()
	elif r == 0:
		r = random.choice(range(0,N))
		
	print '\nRotation of sorted list:\n'

	print 'Number of elements : ', N
	print 'Number of rotations : ', r
	print 'Input dir : ', inputdir
	print 'Output dir : ', outputdir

	# call rotation function
	rotation(N, r, inputdir, outputdir)

if __name__ == "__main__":
   main(sys.argv[1:])
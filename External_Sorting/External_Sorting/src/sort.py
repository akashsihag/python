#!/usr/bin/python

import os
import heapq
import sys, getopt

"""
	author - Akash
	Program - External Sorting
"""

# return list of file in a directory
def file_list(dir):
	return os.listdir(dir)

# create a directory if not exists
def create_dir(dir):
	if not os.path.isdir(dir):
		os.mkdir(dir)

# sort the list
def sort(slice, lines, filename):
	datalist = []
	for line in lines:
		number = line.strip()
		if number:
			datalist.append(int(number))

	datalist.sort() 
	with open("tmp/" + filename.rsplit('/',1)[-1] + str(slice), "w") as fileobj:
		for data in datalist:
			fileobj.write(str(data) + "\n")


def slice_generator(filename, read_size):
	num_slice = (os.path.getsize(filename)/read_size) + 1
	
	with open(filename, 'r') as file:
		for slice in xrange(num_slice):
			lines = file.readlines(read_size)
			sort(slice, lines, filename)


# lazily merge and sort two lists using heapq			
def merge_file(outputdir, count, file):
	files = open('tmp/' + file), open(outputdir + str(count-1) + 'output.txt')
	with open(outputdir + str(count) + 'output.txt', 'w') as writer:
		int_streams = (map(int,f) for f in files)
		int_stream = heapq.merge(*int_streams)
		line_stream = map('{}\n'.format, int_stream)
		writer.writelines(line_stream)
	if count >= 1:
		os.remove(outputdir + str(count-1) + 'output.txt')


# main function
def main(argv):

	inputdir = ''
	outputdir = ''
	memory = 100

	# argument parsing
	try :
		opts, args = getopt.getopt(argv,"hi:o:m:",["ifile=","ofile=","memory="])
	except getopt.GetoptError:
		print 'sort.py -i < inputdir> -o <outputdir> -m <memory in megabytes - default 100 MB>'
		sys.exit(1)
	for opt, arg in opts:
		if opt == '-h':
			print 'sort.py -i < inputdir> -o <outputdir> -m <memory in megabytes - default 100 MB>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputdir = arg
		elif opt in ("-o", "--ofile"):
			outputdir = arg
		elif opt in ("-m", "--memory"):
			memory = int(arg)

	#Print info to the console
	print '\nRunning external sort with following stats:\n'
	print 'Input dir : ', inputdir
	print 'Output dir : ', outputdir
	print 'Memory : ' + str(memory) + ' MB'

	filelist = file_list(inputdir)

	# create a tmp directory for storing intermediate sorted files
	create_dir('tmp/')

	'''
		divide files into multiple slices
		if it file does not fit in memory
		and sort them
	'''
	print '\nInput files :'
	for file in filelist:
		print file
		slice_generator((inputdir + file), int(memory*1024*1024))


	# pick file from tmp folder and merge-sort them using merge_file function
	print '\nSorting input files: '	
	tmpfilelist = file_list('tmp/')
	i = 1
	open(outputdir + str(i-1) + 'output.txt', 'w')
	for file in tmpfilelist:
		print file
		merge_file(outputdir, i, file)
		i += 1

	print '\nAll files sorted and merged...'	
	print 'Output generated in : ' + outputdir + '\n'

if __name__ == "__main__":
   main(sys.argv[1:])

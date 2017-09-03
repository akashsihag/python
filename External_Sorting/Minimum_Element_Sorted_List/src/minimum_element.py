import sys, getopt
import os

"""
	author - Akash
	Program - Rotation of a sorted list.
"""

# finds the minimum element in a given list by using tweaked binary search 
def find_minimum(datalist):
	min = 0
	max = len(datalist) - 1

	while(datalist[min] > datalist[max]):
		mid = (min + max)/2
		if datalist[mid] > datalist[max]:
			min = mid+1
		else:
			max = mid
	return datalist[min]

def main(argv):

	inputdir = ''
	## argument parsing
	try :
		opts, args = getopt.getopt(argv,"hi:",["ifile"])
	except getopt.GetoptError:
		print 'rotate_sorted_list.py -i <input file dir>'
		sys.exit(1)
	for opt, arg in opts:
		if opt == '-h':
			print 'rotate_sorted_list.py -i <input file dir>'
			sys.exit()
		elif opt in ("-i", "--idir"):
			inputdir = arg

	print '\nInput dir : ', inputdir
	print '\nSearching minimum number in the rotated sorted list:\n'

	filelist = os.listdir(inputdir)

	print '\nInput files :\n'
	element_list =  []
	# put all the elements from the input file to a list
	for file in filelist:
		print file
		with open(inputdir + file) as lines:
			for line in lines:
				number = line.strip()
				if number:
					element_list.append(int(number))

	# pass list to the find_minimum function
	if len(element_list) > 0:
		number = find_minimum(element_list)
		print 'Smallest number in the sorted list : ', number
	else:
		print 'List is empty'

if __name__ == "__main__":
   main(sys.argv[1:])

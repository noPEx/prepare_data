#! /usr/bin/python

'''
Given a set of folders as parameters
get the inersection of the files
present in it.
The output is a list of common files
'''


import sys,os


if __name__ == '__main__' :
	number_of_directories = len( sys.argv )
	#print number_of_directories

	if len( sys.argv ) < 3 :
		print 'Usage : python prepare.py dir1 dir2'
		sys.exit()

	directories = sys.argv[1 : ]
	file_lists = []
	#print 'directories are : ',directories

	for directory in directories :
		file_lists.append( os.listdir( directory ) )
		#print file_lists

	intersection_list = file_lists[0]

	#[ intersection_list = list( set( intersection_list ) & set( file_list ) ) for file_list in file_lists ]
	for file_list in file_lists :
		intersection_list = list( set( intersection_list ) & set( file_list ) )
		#print 'int list is : ',intersection_list

	#print 'intersection_list is :'
	print '\n'.join( intersection_list )



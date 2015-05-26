from os import walk
from os import listdir, walk
from os.path import isfile, join
from itertools import izip
import fileinput
import csv

'''
Simple handy functionalities to manipulate and deal with data
from your python code. 
'''

def list_files_with_paths_recursively(mypath):
    """ Recursively list files in mypath and returns the list in the form of ['path/to/file/myfile.extension', '...'] """
    my_files = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        if dirpath[-1] != '/':
            for f in filenames:
                my_files.append(dirpath + '/' + f)
    return my_files

def list_files_in_current_path(path):
    """ Returns files in the current folder only """
    return [ f for f in listdir(path) if isfile(join(path,f)) ]

def find_replace(filename, textToSearch,textToReplace):
    """ finds textToSearch in filename and replaces it with textToReplace """
    i = 0
    for line in fileinput.input(filename, inplace=True):
        sys.stdout.write(line.replace(textToSearch, textToReplace))

def flip_CSV(file):
    """ flips a CSV file within itself (similar to a transpose) """
    a = izip(*csv.reader(open(file, "rb")))
    csv.writer(open(file, "wb")).writerows(a)

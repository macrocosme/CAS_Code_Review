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

def find_replace(fname, text_to_search, text_to_replace):
    """ finds text_to_search in filename and replaces it with text_to_replace within the file fname """
    i = 0
    for line in fileinput.input(fname, inplace=True):
        sys.stdout.write(line.replace(text_to_search, text_to_replace))

def flip_CSV(fname):
    """ flips a CSV file within itself (similar to a transpose) """
    a = izip(*csv.reader(open(fname, "rb")))
    csv.writer(open(fname, "wb")).writerows(a)

from os import walk
from os import listdir, walk
from os.path import isfile, join
from itertools import izip
import fileinput
import csv

from astropy.io import fits
import pyfits
import numpy as np

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

def create_cube_from_files_in_current_folder(out_fname):
    """
    Create a cube from fits files in a folder.

    :param out_fname: output filename (should be .fits)
    :return: nothing.
    """
    #TODO add assert for fits extension; check that all files are in folder are fits... etc.
    files = list_files_in_current_path('.')
    image = fits.open(files[0])
    cube = np.ndarray(shape=(len(files), image[0].data.shape[0], image[0].data.shape[1]), dtype=float)
    i = 0
    for fname in files:
        c = fits.open(fname)
        cube[i] = c[0].data
        i += 1

    header = pyfits.getheader(files[0])
    pyfits.writeto(out_fname, cube, header, clobber=True)

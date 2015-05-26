from os import walk
from os import listdir, walk
from os.path import isfile, join

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

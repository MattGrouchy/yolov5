''' Module to get a list of the file names in a directory '''

import os

def main(dir_name: str):
    ''' return list of files within tree '''
    
    # Get the list of all files in directory tree at given path
    list_of_files = []
    for (dirpath, _, filenames) in os.walk(dir_name):
        list_of_files += [os.path.join(dirpath, file) for file in filenames]
    
    return list_of_files

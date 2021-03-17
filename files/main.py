__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
from zipfile import ZipFile
from pathlib import Path

# Part 1, create dir cache if not exist or clear files if exists
    
def clean_cache():
    dirpath = 'cache'
    if os.path.exists(dirpath):
        FileList = [fileName for fileName in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, fileName))]
        os.chdir(dirpath)
        for filePath in FileList:
            try:
                os.remove(filePath)
            except:
                print("Error while deleting file : ", filePath)
        os.chdir('..')
    else:
        os.mkdir('cache')
    return

# Part 2, unzip files into cache

def cache_zip(zipFileName, cacheDir):
    with ZipFile(zipFileName, 'r') as zipObj:
        zipObj.extractall(path=cacheDir)
    return

# Part 3, make file list with path in absolute terms

def cached_files():
    os.chdir('cache')
    FileList = [os.path.abspath(f) for f in os.listdir() if os.path.isfile(f)]
    os.chdir('..')
    return FileList

# Part 4, find password in textfiles

def find_password(FileList):
    for file in FileList:
        with open(file, "r") as ifile:
            for line in ifile:
                if line.find('password') != -1: return line[line.find(' ') + 1:]
            ifile.close()
    return


# Test part 1
clean_cache()

# Test part 2
cache_zip('data.zip','cache')

# Test part 3
print(cached_files())

# Test part 4
print(find_password(cached_files()))

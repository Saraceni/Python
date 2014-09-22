#! /usr/bin/env python
__author__ = 'Saraceni'
import os
import sys
import fnmatch

def printDirFileNames(dir_path, pattern):
	for path, dirs, files in os.walk(file_path):
		for filename in fnmatch.filter(files, pattern):
			print(os.path.join(path, filename))


file_path = sys.argv[1]
pattern = "*.java"
printDirFileNames(file_path, pattern)

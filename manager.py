from commands import *
from os import listdir, path
from os.path import dirname, realpath, join
from sys import argv

def get_script_dir():
	return dirname(realpath(argv[0]))

def local_filepath(filename):
	return join(get_script_dir(), filename)

extensions = [filename[:-3]
              for filename in listdir(local_filepath("commands"))
              if filename.endswith(".py") and filename != "__init__.py"]

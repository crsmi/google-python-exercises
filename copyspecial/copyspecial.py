#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
  specials = []
  filenames = os.listdir(dir)
  for filename in filenames:
    if re.search('__\w+__', filename):
      specials.append(os.path.abspath(os.path.join(dir,filename)))
  return specials	

def copy_to(paths,dir):
  if not os.path.exists(dir):
    os.makedirs(dir)
  for path in paths:      
    shutil.copy(path,dir)
      
def zip_to(paths, zippath):
  cmd = 'zip\zip -j ' + zippath + ' ' + ' '.join(paths)
  print "Command I'm going to do:" + cmd
  status = subprocess.call(cmd, shell=True)
  if status:
    sys.stderr.write('there was an error: ')
    sys.exit(1)
  
    
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for dir in args:
    print '\n'
    path_list = get_special_paths(dir)
    if todir != '':
      copy_to(path_list, todir)
    elif tozip != '':
      zip_to(path_list, tozip)
    else:      
      for path in path_list:
        print path.encode('string-escape')
	
  
if __name__ == "__main__":
  main()

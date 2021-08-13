import os
with open('changedfile.txt', 'r') as cf:
    files = cf.read()
with open('README.md', 'w') as rm:
    rm.write(files)
os.remove('changedfiles.txt')
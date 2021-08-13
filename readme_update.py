import uuid
with open('changefiles.txt', 'r') as cf:
    files = cf.read()
with open('README.md', 'w') as rm:
    rm.write(files)

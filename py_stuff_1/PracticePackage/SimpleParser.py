import sys


def readinsteps(ind):
    with open('camelot.txt', 'r') as f:
        for line in f:
            print(f.read(ind))


readinsteps(sys.argv[1])
'''
You can do the same with the stdin (no need to use raw_input():

    import sys

for line in sys.stdin:
    do_something()
To complete the picture, binary reads can be done with:

    from functools import partial

with open('somefile', 'rb') as openfileobject:
    for chunk in iter(partial(openfileobject.read, 1024), ''):
do_something()
where chunk will contain up to 1024 bytes at a time from the file.

another one (approximates EOF):
try:
    line = raw_input()
    ... whatever needs to be done incase of no EOF ...
except EOFError:
    ... whatever needs to be done incase of EOF ...
'''
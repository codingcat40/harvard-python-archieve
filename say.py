import sys


from sayings import goodbye, hello

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
    
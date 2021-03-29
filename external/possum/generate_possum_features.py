import sys
import os

print(sys.path)
filename = '../ifeature/data/AAidx.txt'

stream = open(filename)
lines = stream.readlines()
print(lines[:5])
print(os.path.abspath(__file__))

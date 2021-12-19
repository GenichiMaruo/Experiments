import sys
from sys import byteorder
import os

from encode import *
from decode import *

if len(sys.argv) < 2:
    sys.exit(1)

length = 1
nlist = []
files = sys.argv
file = files[1]
with open(file,'rb') as f:
    while b := f.read(length):
        n = int.from_bytes(b, byteorder)
        nlist.append(n)

encode(nlist)

if os.path.exists(file+'.pres'):
	os.remove(file+'.pres')
with open(file+'.pres','wb') as out_file:
    blist = [n.to_bytes(length, byteorder) for n in nlist]
    out_file.writelines(blist)
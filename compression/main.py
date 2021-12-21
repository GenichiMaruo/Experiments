import sys
from sys import byteorder
import os

from encode import *
from decode import *

if len(sys.argv) < 2:
    sys.exit(1)

length = 1
in_list = []
files = sys.argv
file = files[1]
with open(file,'rb') as f:
    while b := f.read(length):
        n = int.from_bytes(b, byteorder)
        in_list.append(n)

out_list = encode(in_list)

if os.path.exists(file+'.pres'):
	os.remove(file+'.pres')
with open(file+'.pres','wb') as out_file:
    blist = [n.to_bytes(length, byteorder) for n in out_list]
    out_file.writelines(blist)
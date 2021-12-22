import sys
from sys import byteorder
import os

from encode import encode
from decode import decode

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

path, ext = os.path.splitext(file)
if ext == '.pres':
    out_list = decode(in_list)
    out_file_name = path
else:
    out_list = encode(in_list, length)
    out_file_name = file+'.pres'

if os.path.isfile(out_file_name):
    if ext == '.pres':
        num = 2
        path2, ext2 = os.path.splitext(out_file_name)
        while os.path.isfile(path2 + ' copy' + str(num) + ext2):
            num += 1
        out_file_name = path2 + ' copy' + str(num) + ext2
    else:
        os.remove(out_file_name)

with open(out_file_name,'wb') as out_file:
    blist = [n.to_bytes(length, byteorder) for n in out_list]
    out_file.writelines(blist)
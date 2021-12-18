import sys
import os

if len(sys.argv) < 2:
    sys.exit(1)

files = sys.argv
file = files[1]
fr = open(file,'rb')



if os.path.exists(file+'.pres'):
	os.remove(file+'.pres')
out_file = open(file+'.pres','wb')
out_file.write(b'abc')
out_file.close()
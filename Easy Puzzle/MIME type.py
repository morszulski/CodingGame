import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

NO_EXT = 'UNKNOWN'
ext_2_mime: dict = dict()

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ext_2_mime[ext.upper()] = mt

for i in range(q):
    fname = input()  # One file name per line.
    print(fname,file=sys.stderr)
    fname_parts = fname.split('.')

    if len(fname_parts) > 1:
        ext = fname_parts[-1].upper()
    else:
        ext = ''

    mt = ext_2_mime.get(ext)
    if not mt:
        mt = NO_EXT
    print(mt)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

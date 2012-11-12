#!/usr/bin/env python

import sys

def main(argv):
    index1 = int(sys.argv[1])
    index2 = int(sys.argv[2])
    try:
        for line in sys.stdin:
            fields = line.split(",")
            if len(fields) > index1 and len(fields) > index2:
                print "UniqValueCount:" + fields[index1] + "\t" + fields[index2]
    except "end of file":
        return None

main(sys.argv)        

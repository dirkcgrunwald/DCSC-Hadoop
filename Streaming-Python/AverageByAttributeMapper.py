#!/usr/bin/env python

import sys

def main(argv):
    try:
        for line in sys.stdin:
            fields = line.split(",")
            if len(fields) < 9:
                print "fields is < 9:", fields
            if (len(fields) > 8 and fields[8] and fields[8].isdigit()):
                print fields[4][1:-1] + "\t" + fields[8]
        return None
    except "end of file":
        return None

main(sys.argv)

#!/usr/bin/python

import sys

hits = 0
oldKey = None

# It will be in the format key\tval
# Where key is the store name, val is the sale amount

for line in sys.stdin:

    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHit = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", hits
        oldKey = thisKey;
        hits = 0

    oldKey = thisKey
    hits += 1

if oldKey != None:
    print oldKey, "\t", hits




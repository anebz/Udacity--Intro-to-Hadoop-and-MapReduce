#!/usr/bin/python

import sys

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

salesTotal = 0
num_sales = 0

for line in sys.stdin:

    num_sales += 1	

    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    salesTotal += float(data_mapped[1])
    

print num_sales, "\t", salesTotal



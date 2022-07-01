#!/usr/bin/env python3

import csv

headers = ['Country', 'State / Province', 'Institution', 'Program']

# read toefl-ibt-home-accepted-schools.csv to a list of list
with open('toefl-ibt-home-accepted-schools.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# remove the first row
data.pop(0)

# drop empty elements in data
for i, entry in enumerate(data):
    data[i] = [x for x in entry if x != '']

# write data to a new csv file named toefl-ibt-home-accepted-schools-clean.csv with header headers
with open('toefl-ibt-home-accepted-schools-clean.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

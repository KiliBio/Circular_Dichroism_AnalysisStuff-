#!/usr/bin/env python
# -*- coding: utf-8 -*-
# crappy_cd_txt_file2csv converter
# Copyright (c) 2018 KiliBio. All rights reserved.

'''
This module converts the crappy txt files, that come out of the most
Circular-Dichroism (CD) Spectrometer Software into analyzable
CSV tables. It can be used as a standalone program.
'''

import csv
import os
import os.path
import re


# sets up the current working directory
cwd = os.getcwd()+"/chem_denat/myoglob/"

# to input file_name
file_name = input("File name: ")
file_name_w_ext = file_name + '.txt'

# try to get non utf-8 characters out, but it didn't worked until now

#txt_file = open(cwd+file_name_w_ext,'r')
#try:
#    for line in txt_file:
#       line = bytes(line, 'utf-8').decode('utf-8', 'ignore')
        #line=line.decode('utf-8','ignore').encode("utf-8")
#except UnicodeDecodeError:
#    bytes(txt_file.readline(), 'utf-8').decode('utf-8', 'ignore')


# line_counter 
num_lines = len(open(cwd+file_name_w_ext).readlines())
#num_lines = sum(1 for line in open(cwd+file_name_w_ext))
#num_lines = os.system("wc -l")


# reads txt_file and writes to csv_file
txt_file = open(cwd+file_name_w_ext,'r')
csv_file = open(cwd+file_name+'.csv', 'w')
csv_writer = csv.writer(csv_file, delimiter = ',')


# I used the regular expression module to get all the whitespaces out and
# cut out all the redundant information
start = 0
for i in range(num_lines):
    line = txt_file.readline()
    if re.search("XYDATA", line):
        start = 1
        csv_writer.writerow(re.split('\s+', line))
    elif start and re.search("#####", line):
        break
    elif start and re.search(r'^\s|\s$', line):
        new_line = re.split('\s+', line)
        replaced_line, floaty_line = [], []

        # for me its convienient to convert the numbers into floats
        for element in new_line: # to be able to convert numbers to floats
            replaced_line.append(re.sub(',','.', element))
        for element in replaced_line: 
            try: # if there are elements that cannot be converted into floats
                floaty_line.append(float(element))
            except ValueError:
                floaty_line.append(element)
        csv_writer.writerow(floaty_line)
    else:
        pass

txt_file.close()
csv_file.close()



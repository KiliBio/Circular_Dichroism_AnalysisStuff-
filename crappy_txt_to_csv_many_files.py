#!/usr/bin/env python
# crappy_cd_txt_file2csv converter
# Copyright (c) 2018 KiliBio. All rights reserved.

# see crappy_txt_to_csv_one_file.py comments

'''
This module converts txt files to CSV tables. It can be used as a standalone
program.
'''
import csv
import os
import os.path
import re

cwd = os.getcwd()+"/chem_denat/myoglob/"

all_txt_files = []
for file in os.listdir(cwd):
    if '.txt' in file:
        all_txt_files.append(file[:-4])
    else:
        pass
print(all_txt_files)

#file_name = input("File name: ")

for file_name in all_txt_files:
    file_name_w_ext = file_name + '.txt'
    num_lines = len(open(cwd+file_name_w_ext).readlines())
    #num_lines = sum(1 for line in open(cwd+file_name_w_ext))
    #num_lines = os.system("wc -l")

    txt_file = open(cwd+file_name_w_ext,'r')
    csv_file = open(cwd+file_name+'.csv', 'w')
    csv_writer = csv.writer(csv_file, delimiter = ',')

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
            for element in new_line:
                replaced_line.append(re.sub(',','.', element))
            for element in replaced_line:
                try:
                    floaty_line.append(float(element))
                except ValueError:
                    floaty_line.append(element)
            csv_writer.writerow(floaty_line)
        else:
            pass

txt_file.close()
csv_file.close()



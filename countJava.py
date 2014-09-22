#! /usr/bin/env python
__author__ = 'Saraceni'
import sys
import re
import fileinput
tot_comment = 0
tot_lines = 0
tot_source = 0
tot_blank = 0
for line in fileinput.input():
	hue = line.split()
	if len(hue)==2:
		opt=hue[0]
		file_name=hue[1]
	else:
		opt="-a"
		file_name=hue[0]
	file = open(file_name, "r")
	num_lines = 0
	source_lines = 0
	comment_lines = 0
	blank_lines = 0
	is_comment = False;
	for line in file:
		num_lines = num_lines + 1
		tot_lines = tot_lines + 1
		if re.match(".*\*//?\n",line):
			is_comment = False;
			comment_lines = comment_lines + 1
			tot_comment = tot_comment + 1
		elif re.match("/\*.*?\n",line) or is_comment==True:
			is_comment = True
			comment_lines = comment_lines + 1
			tot_comment = tot_comment + 1
		elif re.match("^\s+$|\n",line):
			blank_lines = blank_lines + 1
			tot_blank = tot_blank + 1
		elif re.match(" *//.*?\n",line):
			comment_lines = comment_lines + 1
			tot_comment = tot_comment + 1
		else:
			source_lines = source_lines + 1
			tot_source = tot_source + 1


	if opt=="-t":
		print '    {0:3d} (100%)    {1}'.format(num_lines, file_name)
	elif opt=="-s":
		print '    {0:3d} ({1:3d}%)    {2}'.format(source_lines, source_lines*100/num_lines, file_name)
	elif opt=="-b":
		print '    {0:3d} ({1:3d}%)    {2}'.format(blank_lines, blank_lines*100/num_lines, file_name)
	elif opt=="-c":
		print '    {0:3d} ({1:3d}%)    {2}'.format(comment_lines, comment_lines*100/num_lines, file_name)
	else:
		print '   {0:3d} (100%)    {1:3d} ({2:3}%)    {3:3d} ({4:3d}%)    {5:3d} ({6:3d}%)   {7}'.format(num_lines, source_lines, source_lines*100/num_lines, comment_lines, comment_lines*100/num_lines, blank_lines, blank_lines*100/num_lines, file_name)

print '   {0:3d} (100%)    {1:3d} ({2:3}%)    {3:3d} ({4:3d}%)    {5:3d} ({6:3d}%)   TOTAL'.format(tot_lines, tot_source, tot_source*100/tot_lines, tot_comment, tot_comment*100/tot_lines, tot_blank, tot_blank*100/tot_lines)


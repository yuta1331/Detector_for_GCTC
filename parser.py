#!usr/bin/env python
#-*- coding: utf-8 -*-

import re

def html_parser(input_file):
  input_str = ''
  input_list = list()
  for line in open(input_file, 'r'): # read file: html
    input_str = input_str + line
  input_list = re.findall('<td>[0-9]+\.[0-9]+</td>', input_str)
  # input_list = ['<td>0.18</td>', '<td>0.634</td>', '<td>0.692</td>']
  for i, input_reg in enumerate(input_list):
    m = re.search('[0-9]+\.[0-9]+', input_reg)
    if m != None:
      input_list[i] = float(m.group())
  # input_list = [0.18, 0.634, 0.692]
  return input_list

#!usr/bin/env python
#-*- coding: utf-8 -*-

#############################################
# for parsing prev_watermark.html           #
# 2. parse prev_watermark.html              #
# 3. output watermark into output_prev.json #
#############################################

from parser import html_parser

###### parse ######
data_list = html_parser('prev_watermark.html')

print('========== data_list ==========')
# print(len(data_list))
print(data_list)

###### for GUI application ######
import json
outputDict = {
  'data_list' : data_list,
  'extract_bits' : '00000000000000000000000000000000',
  'detected_watermark' : '0'
}
print(outputDict)
outputFile = open('output_prev.json', 'w')
json.dump(outputDict, outputFile)

#!usr/bin/env python
#-*- coding: utf-8 -*-

###########################################
# for detection of watermark              #
# 1. parse watermark.html                 #
# 2. detect data_list                     #
# 3. output watermark into output_wm.json #
###########################################

from detector import detector
from parser import html_parser

###### constant value ######
BITSIZE = 32

###### parse ######
data_list = html_parser('watermarked.html')

print('========== data_list ==========')
# print(len(data_list))
print(data_list)

###### detect ######
returnList = detector(data_list, BITSIZE)
extract_bits = returnList[0]
detected_watermark = returnList[1]

print('========== extract_bits ==========')
# print(len(extract_bits))
print(extract_bits)

print('========== detected_watermark ==========')
print(detected_watermark)

###### for GUI application ######
import json
outputDict = {
  'data_list' : data_list,
  'extract_bits' : extract_bits,
  'detected_watermark' : detected_watermark
}
print(outputDict)
outputFile = open('output_wm.json', 'w')
json.dump(outputDict, outputFile)

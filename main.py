#!usr/bin/env python
#-*- coding: utf-8 -*-

##############################################
# for http request                           #
#  1. get prev_watermark.html                #
#  2. get watermarked.html                   #
#                                            #
# for parsing prev_watermark.html            #
#  1. parse prev_watermark.html              #
#  2. output watermark into output_prev.json #
#                                            #
# for detection of watermark                 #
#  1. parse watermark.html                   #
#  2. detect data_list                       #
#  3. output watermark into output_wm.json   #
##############################################



##############################################
# for http request                           #
#  1. get prev_watermark.html                #
#  2. get watermarked.html                   #
##############################################

import requests

request_org = requests.get("http://mywebpage:8080/org/20733902_2016-11-30.html")
with open("html/prev_watermark.html", "w") as f:
  f.write(request_org.text)

request_mod = requests.get("http://mywebpage:8080/mod/20733902_2016-11-30.html")
with open("html/watermarked.html", "w") as f:
  f.write(request_mod.text)


#############################################
# for parsing prev_watermark.html           #
# 2. parse prev_watermark.html              #
# 3. output watermark into output_prev.json #
#############################################

from parser import html_parser

###### parse ######
data_list = html_parser('html/prev_watermark.html')

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
outputFile = open('output/output_prev.json', 'w')
json.dump(outputDict, outputFile)


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
data_list = html_parser('html/watermarked.html')

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
outputFile = open('output/output_wm.json', 'w')
json.dump(outputDict, outputFile)

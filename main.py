#!usr/bin/env python
#-*- coding: utf-8 -*-

##############################################
# for reading json                           #
#  1. read recommendation.json               #
#  2. figuring home_date                     #
#                                            #
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

import json
import calendar
import requests
from parser import html_parser
from detector import detector
from parser import html_parser

HOST_PORT = "mywebpage:8080"

##############################################
# for reading json                           #
#  1. read recommendation.json               #
#  2. figuring home_date                     #
##############################################

# import json
# import calendar

with open("config_jsons/recommendation.json") as f:
  data = json.load(f)

params = data["params"]
# params = 'params': {'home_no': '10', 'month': '12', 'year': '2016'}

home_dict = {
  0: '15406293',
  1: '15406309',
  2: '15406316',
  3: '15406330',
  4: '17733380',
  5: '17733403',
  6: '17733441',
  7: '17733458',
  8: '18279306',
  9: '18279337',
  10: '18279344',
  11: '19656977',
  12: '20733902',
  13: '20733933',
  14: '21617911',
  15: '21617959',
  16: '22577115',
  17: '22577122',
  18: '22577153',
  19: '22577177',
  20: '22577191',
  21: '25495058'
}

home_date = home_dict[int(params["home_no"])] + "_" + params["year"] + "-" + params["month"] + "-" + "30" # "30" は要検討
# home_date = 20733902_2016-11-30

##############################################
# for http request                           #
#  1. get prev_watermark.html                #
#  2. get watermarked.html                   #
##############################################

# import requests

request_org = requests.get("http://" + HOST_PORT + "/org/" + home_date + ".html")
with open("html/prev_watermark.html", "w") as f:
  f.write(request_org.text)

request_mod = requests.get("http://" + HOST_PORT + "/mod/" + home_date + ".html")
with open("html/watermarked.html", "w") as f:
  f.write(request_mod.text)


#############################################
# for parsing prev_watermark.html           #
# 2. parse prev_watermark.html              #
# 3. output watermark into output_prev.json #
#############################################

# from parser import html_parser

###### parse ######
data_list = html_parser('html/prev_watermark.html')

print('========== data_list ==========')
# print(len(data_list))
print(data_list)

###### for GUI application ######
# import json
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

# from detector import detector
# from parser import html_parser

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
# print(detected_watermark)

###### for GUI application ######
# import json
outputDict = {
  'data_list' : data_list,
  'extract_bits' : extract_bits,
  'detected_watermark' : detected_watermark
}
print(outputDict)
outputFile = open('output/output_wm.json', 'w')
json.dump(outputDict, outputFile)

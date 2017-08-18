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
import requests
from read_json import home_date_from_json
from parser import html_parser
from detector import detector
from parser import html_parser

# HOST_PORT = "mywebpage:8080"
HOST_PORT = ""

# CONFIG_JSON = "config_jsons/recommendation.json"
CONFIG_JSON = ""

##############################################
# for reading json                           #
#  1. read recommendation.json               #
#  2. figuring home_date                     #
##############################################

try:
  home_date = home_date_from_json(CONFIG_JSON)
except:
  print("DEFAULT: homeID_date")
  home_date = home_date_from_json("config_jsons/recommendation.json")

##############################################
# for http request                           #
#  1. get prev_watermark.html                #
#  2. get watermarked.html                   #
##############################################

# import requests

try:
  request_org = requests.get("http://" + HOST_PORT + "/org/" + home_date + ".html")
  with open("html/prev_watermark.html", "w") as f:
    f.write(request_org.text)
except:
  print("DEFAULT: prev_watermark.html")

try:
  request_mod = requests.get("http://" + HOST_PORT + "/mod/" + home_date + ".html")
  with open("html/watermarked.html", "w") as f:
    f.write(request_mod.text)
except:
  print("DEFAULT: watermarked.html")


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

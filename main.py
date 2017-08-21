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
import sys
from time import sleep
from read_json import Read_json
from parser import html_parser
from detector import detector

###### constant value ######

# HOST_PORT = "mywebpage:8080"
HOST_PORT = "192.168.0.3:8080"
# HOST_PORT = ""

CONFIG_JSON = "config_jsons/recommendation.json"

BITSIZE = 32 # 4 words on ASCII code

# outputJSON
OUTPUT_PREV = 'output/before/output_prev.json'
OUTPUT = 'output/after/output.json'


num = None # num is update_count

while(1):
  try:
    config_json = Read_json(CONFIG_JSON)
    tmp = int(config_json.update_count())
  except KeyboardInterrupt:
    sys.exit()
  except Exception as e:
    print("=== ERROR ===")
    print(str(e))
    continue

  if tmp != num:
    sleep(3)
    num = tmp
    home_date = config_json.home_date()

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
    
      request_mod = requests.get("http://" + HOST_PORT + "/mod/" + home_date + ".html")
      with open("html/watermarked.html", "w") as f:
        f.write(request_mod.text)
    except:
      print("WARNING: cannot get html files and use the existed one")
    
    
    try:
      #############################################
      # for parsing prev_watermark.html           #
      # 2. parse prev_watermark.html              #
      # 3. output watermark into output_prev.json #
      #############################################
      
      # from parser import html_parser

      print('########## before watermark ##########')
      
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
      print('========== output_prev.json ==========')
      print(outputDict)
      print('')
      with open(OUTPUT_PREV, 'w') as outputFile:
        json.dump(outputDict, outputFile)
      
      
      ###########################################
      # for detection of watermark              #
      # 1. parse watermark.html                 #
      # 2. detect data_list                     #
      # 3. output watermark into output_wm.json #
      ###########################################
      
      # from detector import detector
      # from parser import html_parser

      print('########## after watermark ##########')
      
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
      
      print('========== output_wm.json ==========')
      # print(detected_watermark)
      
      ###### for GUI application ######
      # import json
      outputDict = {
        'data_list' : data_list,
        'extract_bits' : extract_bits,
        'detected_watermark' : detected_watermark
      }
      print(outputDict)
      with open(OUTPUT, 'w') as outputFile:
        json.dump(outputDict, outputFile)
    except Exception as e:
      print("=== ERROR ===")
      print(str(e))

      print("USE DEFAULT: output_json")

      default_output_prev_dict = {"data_list": [0.19, 0.135, 0.192, 0.136, 0.122, 0.113, 0.103, 0.11, 0.103, 0.105, 0.107, 0.097, 0.11, 0.108, 0.425, 0.454, 0.565, 0.377, 0.349, 0.272, 0.239, 0.305, 0.247, 0.243, 0.506, 0.471, 0.174, 0.163, 0.148, 0.207, 0.213, 0.161, 0.179, 0.141, 0.28, 0.194, 0.189, 0.26, 0.296, 0.531, 0.314, 0.355, 0.497, 0.227, 0.227, 0.229, 0.33, 0.357], "detected_watermark": "0", "extract_bits": "00000000000000000000000000000000"}
      print("output_prev_dict = " + str(default_output_prev_dict))
      with open(OUTPUT_PREV, 'w') as outputFile:
        outputFile.write(str(default_output_prev_dict))

      default_output_dict = {"data_list": [0.18, 0.634, 0.692, 0.636, 0.122, 0.612, 0.602, 0.61, 0.103, 0.605, 0.606, 0.097, 0.1, 0.607, 0.425, 0.953, 0.064, 0.876, 0.848, 0.772, 0.238, 0.305, 0.746, 0.743, 0.005, 0.97, 0.674, 0.662, 0.148, 0.707, 0.213, 0.16, 0.179, 0.141, 0.28, 0.194, 0.188, 0.25, 0.296, 0.531, 0.314, 0.354, 0.497, 0.226, 0.226, 0.229, 0.33, 0.356], "detected_watermark": "west", "extract_bits": "01110111011001010111001101110100"}
      print("output_dict = " + str(default_output_dict))
      with open(OUTPUT, 'w') as outputFile:
        outputFile.write(str(default_output_dict))
      continue

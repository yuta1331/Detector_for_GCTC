#!usr/bin/env python
#-*- coding: utf-8 -*-

from detector import *
from parser import html_parser

###### constant value ######
BITSIZE = 32

###### parse ######
data_list = html_parser('watermarked.txt')
print('########## data_list ##########')
print(data_list)

###### detect ######
detected_watermark = detector(data_list, BITSIZE)
print('########## detected_watermark ##########')
print(detected_watermark)

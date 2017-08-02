#!usr/bin/env python
#-*- coding: utf-8 -*-

from detector import *
from parser import html_parser

if __name__ == '__main__':
  input_list = html_parser('watermarked.txt')
  print(input_list)

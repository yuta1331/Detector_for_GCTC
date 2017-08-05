#!usr/bin/env python
#-*- coding: utf-8 -*-

# input_list = ['<td>0.18</td>', '<td>0.634</td>', '<td>0.692</td>']

import math

def detector(input_list, bitsize):
  extract_bits = ''
  for i, input_value in enumerate(input_list):
    if (i == bitsize): break
    extract_bit = '0' if (input_value - int(input_value)) < 0.5 else '1'
    extract_bits = extract_bits + extract_bit
 # extract_bits = '01110111011001010111001101110100'
  print('========== extract_bits ==========')
  # print(len(extract_bits))
  print(extract_bits)

  detect_word = ''
  for i in range(math.ceil(bitsize / 8)): # math.ceil(bitsize / 8) : the number of detect_word
    ascii_bin = extract_bits[i*8:(i+1)*8] # ascii_bin = '01110111'
    ascii_dec = int(ascii_bin, 2) # ascii_dec = 119
    detect_word = detect_word + chr(ascii_dec) # detect_word = west
  return detect_word

if __name__ == '__main__':
  BITSIZE = 32
  INPUT_LIST = [0.18, 0.634, 0.692, 0.636, 0.122, 0.612, 0.602, 0.61, 0.103, 0.605, 0.606, 0.097, 0.1, 0.607, 0.425, 0.953, 0.064, 0.876, 0.848, 0.772, 0.238, 0.305, 0.746, 0.743, 0.005, 0.97, 0.674, 0.662, 0.148, 0.707, 0.213, 0.16, 0.179, 0.141, 0.28, 0.194, 0.188, 0.25, 0.296, 0.531, 0.314, 0.354, 0.497, 0.226, 0.226, 0.229, 0.33, 0.356]
  result = detector(INPUT_LIST, BITSIZE)
  print(result)

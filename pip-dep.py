#!usr/bin/env python
#-*- coding: utf-8 -*-


if __name__ == '__main__':
    with open('dependencies.txt','r') as f:
         line = ' '.join([l.rstrip('\n') for l in f.readlines()])
    print(line)

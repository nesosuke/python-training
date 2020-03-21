#!/usr/bin/python3
import sys
filepath = sys.argv[1]
open(filepath, 'a').write(input())
open(filepath, 'a').write('\n')
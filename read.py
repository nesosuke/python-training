#!/usr/bin/python3
import sys
args = sys.argv[1]
# filepath = input()  // コマンドライン上で引数にしたい
print(open(args, "r").read())
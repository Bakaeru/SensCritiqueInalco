#! /usr/bin/python3
#! coding: utf-8

import json, pprint

def open_and_read(infile):
	f=open(infile)
	a=json.load(f)
	pprint(a)

if __name__ == '__main__':
	open_and_read("corpus.json")
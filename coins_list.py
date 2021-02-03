#!/usr/bin/python

#the program provides the file table_coins_list.csv which contains the list of coins IDs in coingecko

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

import sys

import csv

import time


coins_list=cg.get_coins_list()

with open('/home/pippo/python/pycoingecko/table_coins_list.csv','wt') as fh:
	csvobj=csv.DictWriter(fh,fieldnames=list(coins_list[0].keys()))
	csvobj.writeheader()
	csvobj.writerows(coins_list)

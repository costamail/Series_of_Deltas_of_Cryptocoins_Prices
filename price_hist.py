#!/usr/bin/python

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

import sys

import csv

import time

import datetime
today0=datetime.date.today()
today1=str(today0.day)+'-'+str(today0.month)+'-'+str(today0.year)


import csv



#Below it reads the second parameter with numbers of days as of today and 
#they are the deltas in days for the counting of the price variation in percentage
delta_array=[]
days_filename=str(sys.argv[2])
with open(days_filename,'rt') as fh:
	temp_days_list=fh.readline()
	temp_days_list=temp_days_list.strip('\n')
	temp_days_list=temp_days_list.split(',')
	for day_amount in temp_days_list:		
		day_amount=day_amount.strip()
		if not day_amount.isnumeric():
			continue
		day_amount=int(day_amount)
		delta_array.append(day_amount)

ll=[]

date_keys=[]
pastdate_array=[]

for i in delta_array:
	x=datetime.timedelta(days=i)
	y=today0-x
	y=str(y.day)+'-'+str(y.month)+'-'+str(y.year)
	pastdate_array.append(y)
	date_key=str(i) + ' days'
	date_keys.append(date_key)
	
print("the deltas in days for the counting of the price variation in percentage are ", date_keys)


# the function below returns the coin price for the serie of dates
def percent(coin,date):
	int_coin=coin
	#print(int_coin,'dentropercent')
	int_date=date
	array_price_inpast=cg.get_coin_history_by_id(int_coin,int_date)
	if not 'market_data' in array_price_inpast.keys():
		return None
	else:
		price_inpast=array_price_inpast['market_data']['current_price']['eur']
	array_price_today=cg.get_coin_history_by_id(int_coin,today1)
	price_today=array_price_today['market_data']['current_price']['eur']	
	T=price_today
	P=price_inpast
	pc=((T-P)/P)*100
	pc=round(pc,2)
	return pc
	
#This opens the file containg the list of coins	
filename=str(sys.argv[1])
rows=[]
with open(filename,'rt') as fh:
	rows=fh.readlines()
coin_rows=[]
for row in rows:
	row=row.rstrip('\n')
	if row!='':
		coin_rows.append(row)
print('The list of cryptocoins ' , coin_rows)




for loop_coin in coin_rows:
	diz={}
	diz['coin']=loop_coin
	#print(loop_coin, ' dentro loop_coin')
	#loop_pc_array={}
	#for key in date_keys:
	#	loop_pc_array[key]=None
	for key,loop_date in zip(date_keys,pastdate_array):
		time.sleep(1)
		#print(loop_date)
		percent_number=percent(loop_coin,loop_date)
		#print(percent_number, ' dentro loop_date')
		diz[key]=percent_number
	ll.append(diz)


#Creates the csv file with the table
with open('tabelle_price_history.csv','wt') as fh:
	csvobj=csv.DictWriter(fh, list(ll[0].keys()))
	csvobj.writeheader()
	csvobj.writerows(ll)






'''

'''



















	


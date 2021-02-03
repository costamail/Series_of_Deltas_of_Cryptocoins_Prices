# Series_of_Deltas_of_Cryptocoins_Prices
Series of Deltas in Percentage of Cryptocoins Prices

The file price_hist.py provides the csv file tabelle_price_history.csv with the table which contains the deltas in percentage of the current price of the cryptocoins

You have to put the list of ids of the coins in one txt file: one id of coins per line 
You can get the list of the ids of the coin by runnig the program coins_list.py and you get the file table_coins_list.csv. 

$python3 coins_list.py

and you get the file table_coins_list.csv. 
You need to install the package pycoingecko before running it
You open table_coins_list.csv and the first column is the id, the second colum is the symbol, the hitrd column is the name
You choose the coins and out the ids in the file for the coin list
For example you create the txt file coins.txt and you put each id of coin per line like below ( I have out the escape '\n' for the ewn line becasue the README does not allow to ouput the new line)

'ethereum\nbitcoin\npolkadot\nchainlink\nuniswap\n'

Then you had to prepare the second txt file with the deltas of time , each delta is indicated in number of days as of today and you have to put the list of amount of days in the first row of the txt file and of course the numbers separated by comma like below

1,7,14,21,30,60,90,120,150,180,360,720,

Then let's say that the file with the coin list is coins.txt and the txt file with the deltas of days as of today is list_of_days.txt
When you run the program price_hist.py you have to give two parameters: the first is the file with the coin list and the second is the txt file with the deltas of days as of today
You ran it like below  

$ python3 price_hist.py short_coins.txt list_of_days.txt 

and you get the csv file tabelle_price_history.csv

In tabelle_price_history.csv the first column is the coin name, then the following columns contain the price delta in percentage compared to the today price



import csv
import math

# File: TradeProcessor.py
# Author: Jared Allmaras
# Date Created: 10/26/2018
# Date Last Modified: 10/26/2018	

def process_trades(trade_list, symbol_list):
	result_list = []

	# O(n * m) solution where n is the number of rows in the CSV and m is the
	# number of unique 3 character symbols (capped at 26^3). Therefore, the  
	# solution, when approaching infinity, can be simplified to O(n).
	for symbol in symbol_list:
		prev_time_stamp = 0
		max_time_gap = 0
		volume = 0
		max_price = 0
		weighted_total = 0

		for trade in trade_list:
			if symbol == trade[1]:
				time_stamp = int(trade[0])
				if prev_time_stamp == 0:
					prev_time_stamp = time_stamp
				else:
					max_time_gap = max(max_time_gap, 
									  (time_stamp - prev_time_stamp))
					prev_time_stamp = time_stamp
				volume += int(trade[2])
				max_price = max(max_price, int(trade[3]))
				weighted_total += (int(trade[2]) * int(trade[3]))
		
		weighted_avg_price = weighted_total // volume
		result_list.append([symbol, max_time_gap, volume, weighted_avg_price, 
							max_price])

	return result_list

def main():	
	trade_list = []
	symbol_list = []

	# Reads in CSV file of trades
	# Row[0] = time_stamp of trade in microseconds since midnight
	# Row[1] = 3 Character unique symbol for the financial instrument
	# Row[2] = quantity or amount to be traded
	# Row[3] = price of the trade for that financial instrument 
	with open('input.csv', 'r') as csv_file:
		data_reader = csv.reader(csv_file, delimiter=',')
		# copies in data from CSV and creates 2 lists: a list of all the rows 
		# and a list of each unique three character symbol 
		for row in data_reader:
			trade_list.append(row)
			if row[1] not in symbol_list:
				symbol_list.append(row[1])
		# sort the symbol_list and process the trades in alphabetical order in
		# order to preemptively sort output 
		symbol_list.sort()		
	result_list = process_trades(trade_list, symbol_list)

	#writes the results of trades for the day back into file 'output.csv'
	with open('output.csv', 'w', newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		for result in result_list:
			csv_writer.writerow(result)
			
if __name__ == '__main__':
	main()
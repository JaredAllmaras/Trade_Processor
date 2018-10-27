import unittest
import csv
from TradeProcessor import process_trades

# File: test_TradeProcessor.py
# Author: Jared Allmaras
# Date Created: 10/26/2018
# Date Last Modified: 10/26/2018

class TestTradeProcessor(unittest.TestCase):


	def setUp(self):
		self.input_file = 'test_input.csv'
		self.output_file = 'test_output.csv'
		self.test_trade_list = []
		self.test_symbol_list = []
		self.expected_result_list = []

		# reads in input from CSV file to test against expected output
		with open(self.input_file, 'r') as csv_file:
			data_reader = csv.reader(csv_file, delimiter=',')
			for row in data_reader:
				self.test_trade_list.append(row)
				if row[1] not in self.test_symbol_list:
					self.test_symbol_list.append(row[1])
			self.test_symbol_list.sort()

		# reads in expected output from CSV file and saves to 
		# expected_result_list
		with open(self.output_file, 'r') as csv_file:
			data_reader = csv.reader(csv_file, delimiter=',')
			for row in data_reader:
				self.expected_result_list.append([row[0], int(row[1]), 
												 int(row[2]), int(row[3]), 
												 int(row[4])])

	def test_process_trades(self):
		for row in self.expected_result_list:
			self.assertEqual(process_trades(self.test_trade_list, 
											self.test_symbol_list), 
											self.expected_result_list)
			

if __name__ == '__main__':
	unittest.main()
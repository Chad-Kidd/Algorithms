#!/usr/bin/python

import argparse
import math
#find max profit from list of stock prices
#evaluate high and low to find max difference
#sell at high number
testing_price_list = [78, 1, 3, 0, 75, 86, 106]

def find_max_profit(prices): #receives as input a list of stock prices
  #use iterative sorting
  max_profit = prices[1] - prices[0]
  # pass
  for i in range[1, len(prices)]: #pass prices
    #iterate from 1 to -1 using for-loop
    #have to sell on first element
    #iterate to end of prices
    #figure out some type of formulate to get 
    #max profit that can be made from a single buy and sell. 
    #You must buy first before selling

  return max_profit

print(find_max_profit(testing_price_list))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()
  parser.add_argument('--dry-run', action='store_true')

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
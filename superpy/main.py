# Imports
import argparse
import csv
from datetime import date, timedelta

# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


# Your code below this line.
def main():

	# Define argument parser

	my_parser = argparse.ArgumentParser(description='SuperPy')

	my_parser.add_argument('CLIcommand', 
			type=str, 
			help='command')

	my_parser.add_argument('--product-name', 
                    help=', product name', 
                    action='store', 
                    type=str)

	my_parser.add_argument('--price', 
                    help=', product price', 
                    action='store', 
                    type=float)

	my_parser.add_argument('--expiration-date', 
                    help=', product expiration date', 
                    action='store', 
                    type=str)

	my_parser.add_argument('--date', 
                    help=', date', 
                    action='store', 
                    type=str)

	my_parser.add_argument('--now', 
                    help=', date today', 
                    action='store_const', 
                    const=date.today().strftime("%Y-%m-%d"))

	my_parser.add_argument('--today', 
                    help=', date today', 
                    action='store_const', 
                    const=date.today().strftime("%Y-%m-%d"))

	my_parser.add_argument('--yesterday', 
                    help=', date yesterday', 
                    action='store_const', 
                    const=(date.today() - timedelta(days=1)).strftime("%Y-%m-%d"))

	# Check arguments

	args = my_parser.parse_args()
	print(vars(args))
	if args.CLIcommand.lower() not in ['buy','sell','report']:
	    print(False)
	else:
	    print(True)

	return




if __name__ == '__main__':
    main()

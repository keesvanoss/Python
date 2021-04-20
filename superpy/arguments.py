import argparse

def get_arguments():
    
    my_parser = argparse.ArgumentParser(description='SuperPy')

    my_parser.add_argument('CLI_command', 
		            nargs='?',
		            default='None', 
                    type=str, 
		            help='user command')

    my_parser.add_argument('report_name', 
		            nargs='?',
		            default='None', 
                    type=str,
                    help='report name')

    my_parser.add_argument('--product-name', 
                    help=', product name', 
                    action='store', 
                    type=str)

    my_parser.add_argument('--price', 
                    help=', product price', 
                    action='store', 
                    type=float)

    my_parser.add_argument('--advance-time', 
                    help=', advance time in days', 
                    action='store', 
                    type=int)

    my_parser.add_argument('--expiration-date', 
                    help=', product expiration date', 
                    action='store', 
                    type=str)

    my_parser.add_argument('--buy-date', 
                    help=', product bought date', 
                    action='store', 
                    type=str)

    my_parser.add_argument('--date', 
                    help=', date', 
                    action='store', 
                    type=str)

    my_parser.add_argument('--now', 
                    help=', current date', 
                    action='store_const', 
                    const=True)

    my_parser.add_argument('--today', 
                    help=', current date', 
                    action='store_const', 
                    const=True)

    my_parser.add_argument('--yesterday', 
                    help=', date yesterday', 
                    action='store_const', 
                    const=True)

    return my_parser.parse_args()
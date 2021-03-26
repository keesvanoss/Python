# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'

#---------------------------------------------------------------------------------------------
# Declare import modules
#---------------------------------------------------------------------------------------------

import report, arguments, sys, datetime

# Your code below this line.

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

def buy(product_name, price, expiration_date):
    print(product_name, price, expiration_date)
    return

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

def sell(product_name, price):
    print(product_name, price)
    return

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

def advance_time(skip_days):
    print(skip_days)
    return

#---------------------------------------------------------------------------------------------
# Check date to be sure it's a valid date in the right format.
# If ok, return date, else return None
#---------------------------------------------------------------------------------------------

def check_date(input_date):
    try:
        format = "%Y-%m-%d"
        datetime.datetime.strptime(input_date, format)
        return input_date
    except:
        print("ERROR: This is an incorrect date string format <YYYY-MM-DD>")
        return None
    return

#---------------------------------------------------------------------------------------------
# Main routine
#---------------------------------------------------------------------------------------------

def main():
    
    # Get command line arguments
    args = arguments.get_arguments()

    # Check if command is buy, if so then execute the buy routine
    if args.CLI_command.lower() == 'buy':
        
        # Check if date is given and if so, if format is ok
        report_date = None
        if args.yesterday != None: 
            report_date = args.yesterday
        elif args.now != None: 
            report_date = args.now
        elif args.today != None: 
            report_date = args.today
        elif args.date != None:
            report_date = check_date(args.date)
        else:
            print('ERROR: Missing data: buy <product_name> <price> <expiration_date>')
            return
        
        # If date ok then execute buy routine else exit routine
        if report_date != None: 
            buy(args.product_name, args.price, report_date)
        else:
            return
    
    # Check if command is sell, if so then execute the sell routine
    elif args.CLI_command.lower() == 'sell': sell(args.product_name, args.price)
    
    # Check if command is report, if so then execute the report routine
    elif args.CLI_command.lower() == 'report':
        
        # Check if date is given and if so, if format is ok
        report_date = None
        if args.yesterday != None: 
            report_date = args.yesterday
        elif args.now != None: 
            report_date = args.now
        elif args.today != None: 
            report_date = args.today
        elif args.date != None: 
            report_date = check_date(args.date)
        else:
            print('ERROR: Missing data: report <report_name> <date>')
            return
       
        # If date ok then show report else exit routine
        if report_date != None: 
            print(report.show_report(args.report_name, report_date))
            return 'Ok'
        else:
            return
        
    # Check if command is buy, if so then execute the buy routine
    elif args.advance_time != None: advance_time(args.advance_time)
    
    # Unknown command
    else:
        print(f"ERROR: unknown command '{args.CLI_command}' <buy, sell, report>")
    return

if __name__ == '__main__':
    main()

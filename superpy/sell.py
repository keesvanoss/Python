import csv, pathlib, os
from utils import check_date
from files import read_bought, read_sold, clearfile
from datetime import datetime

csv_outputfile = 'sold.csv'

#---------------------------------------------------------------------------------------------
# Syntax: sell product_name, sell_date, price
# Data will be added to the sold.csv file with an ID
#---------------------------------------------------------------------------------------------

def sell(product_name, sell_date, price):
    
    # Convert report date to date object
    try:
        sold_date = datetime.strptime(sell_date.strip("'"),'%Y-%m-%d')
    except:
        return 'ERROR, Wrong date format'

    # Check if routine is called with the right parameters    
    error_message = ''
    if product_name == None:
        error_message += "ERROR: missing argument --product_name\n"
    if check_date(sell_date) == None:
        error_message += "ERROR: missing argument --sell_date or wrong format <YYYY-MM-DD>\n"
    if price == None:
        error_message += "ERROR: missing argument --price\n"
    
    # If parameters ok, add data to sold.csv file
    if error_message == '':

        # If sold.csv exists, read last id nr else id = 0
        file = pathlib.Path(csv_outputfile)
        if file.exists ():
            with open(csv_outputfile,'r') as f:
                opened_file = f.readlines()
                id = int(opened_file[-1].split(',')[0] )
                id = id + 1
        else:
            id = 0

        bought = read_bought(sell_date)
        
        # If items sold then update bought list
        if id > 0:

            # Check if product in stock

            # Read products sold and remove sold products from bought list
            sold = read_sold(sell_date)
            for item in sold.items():
                product_sell_date = datetime.strptime(item[1][1].strip("'"),'%Y-%m-%d')

                # If sell_date is before report_date, remove item from bought list
                if product_sell_date <= sold_date:
                    if item[1][0] in bought:
                        del bought[item[1][0]]

        # Check if product available
        product_id = -1
        for item in bought.items():
            if item[1][0] == product_name:
                product_id = item[0]
                break
        
        if product_id != -1:
            # Write data row with id to csv file
            with open(csv_outputfile, mode='a', newline='', encoding='utf-8') as f:
                product_writer = csv.writer(f, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
                product_writer.writerow([id, int(product_id), sell_date, price])
            
            # Action finished without problems, return 'Ok'
            return 'Ok'
        else:
            return 'ERROR: Product not in stock'
    else:
        
        # Error occured, return error
        return error_message




# Test routine

def main():
    
    clearfile('sold.csv')
    
    #Test call with missing parameters
    print('Testing input1:')
    print(sell(None, None, None))
    print('Testing input2:')
    print(sell('Orange', None, None))
    print('Testing input3:')
    print(sell(None, None, 4))
    
    #Add 4 items to sell.csv
    print('Testing adding data:')
    print(sell('Orange', '2021-01-04', 3))
    print(sell('Apple', '2021-01-04', 2))
    print(sell('Peer', '2021-01-04', 4))
    print(sell('Orange', '2021-02-01', 4))
    
    return



if __name__ == '__main__':
    main()
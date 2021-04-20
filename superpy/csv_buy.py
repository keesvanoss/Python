import csv, pathlib, os
from utils import check_date, cleardata

csv_outputfile = 'bought.csv'

#---------------------------------------------------------------------------------------------
# Syntax: buy product_name, price, expiration_date
# Data will be added to the bought.csv file with an iId
#---------------------------------------------------------------------------------------------

def buy(product_name, buy_date, price, expiration_date):
    
    # Check if routine is called with the right parameters    
    error_message = ''
    if product_name == None:
        error_message += "ERROR: missing argument --product-name\n"
    if price == None:
        error_message += "ERROR: missing argument --price\n"
    if check_date(expiration_date) == None:
        error_message += "ERROR: missing argument --expiration-date or wrong format <YYYY-MM-DD>\n"
    if check_date(buy_date) == None:
        error_message += "ERROR: missing argument --buy-date or wrong format <YYYY-MM-DD>"

    # If parameters ok, add data to bought.csv file
    if error_message == '':
        
        # If bought.csv exists, read last id nr else id = 0
        file = pathlib.Path(csv_outputfile)
        if file.exists ():
            with open(csv_outputfile,'r') as f:
                opened_file = f.readlines()
                id = int(opened_file[-1].split(',')[0] )
                id = id + 1
        else:
            id = 0

        # Write data row with id to csv file
        with open(csv_outputfile, mode='a', newline='', encoding='utf-8') as f:
            product_writer = csv.writer(f, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
            product_writer.writerow([id, product_name, buy_date, price, expiration_date])
        
        # Action finished without problems, return 'Ok'
        return 'Ok'
    
    else:
        
        # Error occured, return error
        return error_message




# Test routine

def main():
    
    # If bought.csv and sold.csv exists, delete them
    cleardata()

    # Test call with missing parameters
    print('Testing input1:')
    print(buy(None, None, None, None))
    
    print('\nTesting input2:')
    print(buy('Orange', None, None, None))
    
    print('\nTesting input3:')
    print(buy(None, None, 4, None))
    
    print('\nTesting input4:')
    print(buy('Orange', '2021-03-13', 4, None))
    
    print('\nTesting input5:')
    print(buy(None, '2021-03-13', None, '2021-03-11'))
    
    print('\nTesting input6:')
    print(buy('Orange', '2021-03-13', None, '2021-03-11'))
    
    print('\nTesting input7:')
    print(buy(None, '2021-03-13', 4, '2021-03-11'))
    
    print('\nTesting input8:')
    print(buy(None, '2021-03-13', 4, '2021-03-81'))
   
    # Add 3 items to bought.csv
    print('\nTesting adding data:')
    print(buy('Orange', '2021-03-13', 3, '2021-03-27'))
    print(buy('Apple', '2021-03-13', 2, '2021-03-27'))
    print(buy('Peer', '2021-03-13', 4, '2021-03-25'))
    print(buy('Peer', '2021-03-13', 4, '2021-03-28'))
    
    return



if __name__ == '__main__':
    main()

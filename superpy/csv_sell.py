import csv, pathlib, os
from utils import check_date, cleardata

csv_outputfile = 'sold.csv'

#---------------------------------------------------------------------------------------------
# Syntax: sell product_name, price
# Data will be added to the sold.csv file with an Id
#---------------------------------------------------------------------------------------------

def sell(product_name, sell_date, price):
    
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

        # Check if product in stock



        # Write data row with id to csv file
        product_id = 0
        with open(csv_outputfile, mode='a', newline='', encoding='utf-8') as f:
            product_writer = csv.writer(f, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
            product_writer.writerow([id, product_id, sell_date, price])
        
        # Action finished without problems, return 'Ok'
        return 'Ok'
    
    else:
        
        # Error occured, return error
        return error_message




# Test routine

def main():
    
    cleardata('sold.csv')
    
    #Test call with missing parameters
    print('Testing input1:')
    print(sell(None, None, None))
    print('Testing input2:')
    print(sell('Orange', None, None))
    print('Testing input3:')
    print(sell(None, None, 4))
    
    #Add 3 items to bought.csv
    print('Testing adding data:')
    print(sell('Orange', '2021-01-04', 3))
    print(sell('Apple', '2021-01-04', 2))
    print(sell('Peer', '2021-01-04', 4))
    
    return



if __name__ == '__main__':
    main()
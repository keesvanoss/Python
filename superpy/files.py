import csv, pathlib, os
from datetime import datetime

# Read products bought
def read_bought(compare_date):

    #print (compare_date)
    # Convert compare date to date object
    try:
        compare_date = datetime.strptime(compare_date.strip("'"),'%Y-%m-%d')
    except:
        return 'ERROR, Wrong date format'

    filename='bought.csv'
    bought = {}

    f = pathlib.Path(filename)
    if f.exists ():
        f = open(filename)
        reader = csv.reader(f)
        with f:
            for row in reader:
                product_id, product_name, buy_date, price, exp_date = row
                chk_date = datetime.strptime(buy_date.strip("'"),'%Y-%m-%d')
                if chk_date <= compare_date:
                    bought[product_id] = [product_name.replace("'", ""), buy_date, float(price), exp_date]
    else:
        return f"ERROR: can't open {filename}"
    return bought

# Read products sold
def read_sold(compare_date):

    # Convert compare date to date object
    try:
        compare_date = datetime.strptime(compare_date.strip("'"),'%Y-%m-%d')
    except:
        return 'ERROR, Wrong date format'

    filename='sold.csv'
    sold = {}

    f = pathlib.Path(filename)
    if f.exists ():
        f = open(filename)
        reader = csv.reader(f)
        with f:
            for row in reader:
                product_id, sell_id, sold_date, price = row
                chk_date = datetime.strptime(sold_date.strip("'"),'%Y-%m-%d')
                if chk_date <= compare_date:
                    sold[product_id] = [sell_id, sold_date, sold_date, float(price)]
    else:
        return f"ERROR: can't open {filename}"
    return sold

#---------------------------------------------------------------------------------------------
# Clear datafile
#---------------------------------------------------------------------------------------------

def clearfile(filename):
    file = pathlib.Path(filename)
    try:
        if file.exists ():
            os.remove(file)
        return f"File {filename} is erased"
    except:
        return f"ERROR, can't erase file {filename}"

def main():
    
    # print('Test reading bought.csv into list:')
    # print(read_bought('2021-01-03'))
    # print('\nTest reading sold.csv into list:')
    # print(read_sold('2021-01-04'))
    print(clearfile('bought.csv'))
    print(clearfile('sold.csv'))


if __name__ == '__main__':
    main()
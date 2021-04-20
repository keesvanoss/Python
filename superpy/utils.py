import datetime, pathlib, os
import csv


#const=date.today().strftime("%Y-%m-%d"))
#const=date.today().strftime("%Y-%m-%d"))
#const=(date.today() - timedelta(days=1)).strftime("%Y-%m-%d"))

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
        return None

# Read current date from config.txt and convert to string 'YYYY-mm-dd'
# Date is stored in config.txt as Year, Month, Dat

def get_current_date():
    file = pathlib.Path('config.txt')
    if file.exists ():
        with open('config.txt', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                current_date = datetime.datetime(int(row[0]), int(row[1]), int(row[2]))
            return current_date.strftime('%Y-%m-%d')  
    else:
        return 'ERROR: config.txt does not exist.'

# Clear data files for testing

def cleardata():
    file = pathlib.Path('bought.csv')
    if file.exists ():
       os.remove(file)
    
    file = pathlib.Path('sold.csv')
    if file.exists ():
       os.remove(file)

    return
# Test routine

def main():
    
    # Check datum
    print('Test1: ', check_date(None) == None)
    print('Test2: ', check_date('test') == None)
    print('Test3: ', check_date('2021-03-90') == None)
    print('Test4: ', check_date('2021-03-10') == '2021-03-10')
    print('Test5: ', get_current_date() == datetime.datetime(2021, 3, 29))
    
    return


if __name__ == '__main__':
    main()


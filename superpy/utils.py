import pathlib, os
import csv
from datetime import date, timedelta, datetime

#---------------------------------------------------------------------------------------------
# Check date to be sure it's a valid date in the right format.
# If ok, return date, else return None
#---------------------------------------------------------------------------------------------

def check_date(input_date):

    try:
        format = "%Y-%m-%d"
        datetime.strptime(input_date, format)
        return input_date
    except:
        return None

#---------------------------------------------------------------------------------------------
# Read current date from config.txt and convert to string 'YYYY-mm-dd'
# Date is stored in config.txt as Year, Month, Dat
#---------------------------------------------------------------------------------------------

def get_current_date():
    file = pathlib.Path('config.txt')
    if file.exists ():
        with open('config.txt', newline='') as f:
            curdate=''
            reader = csv.reader(f)
            for row in reader:
                curdate = datetime(int(row[0]), int(row[1]), int(row[2]))
            return curdate.strftime('%Y-%m-%d')  
    else:
        return 'ERROR: config.txt does not exist.'

#---------------------------------------------------------------------------------------------
# Advance date xx days and save year,month,day in config.txt
#---------------------------------------------------------------------------------------------

def advance_date(days):
    
    # Read current date and add days to it
    date = get_current_date()
    date = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=days)).strftime('%Y-%m-%d')
    
    # Write current date back to config.txt
    year = date[:4]
    month = date[5:7]
    day = date[8:]
    with open('config.txt', 'w') as f:
        f.write(year + ',' + month + ',' + day)
    
    return f'Current date: {date}'

#---------------------------------------------------------------------------------------------
# Set current date to a certain date and save year,month,day in config.txt
#---------------------------------------------------------------------------------------------

def set_date(date):
    
    # Write current date back to config.txt
    year = date[:4]
    month = date[5:7]
    day = date[8:]
    with open('config.txt', 'w') as f:
        f.write(year + ',' + month + ',' + day)
    
    return f'Current date: {date}'

#---------------------------------------------------------------------------------------------
# Test routine
#---------------------------------------------------------------------------------------------

def main():
    
    #Check date utils
    print(set_date('2021-01-01'))
    print(advance_date(2))
    # print('Test3: ', check_date('2021-03-90') == None)
    # print('Test4: ', check_date('2021-03-10') == '2021-03-10')
    # print('Test5: ', get_current_date() == datetime.datetime(2021, 3, 29))
    # advance_date(2)   
    return


if __name__ == '__main__':
    main()


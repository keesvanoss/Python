import csv
from datetime import date, timedelta, datetime

#---------------------------------------------------------------------------------------------
# Report inventory on certain date
#---------------------------------------------------------------------------------------------
# Return list with products in store and expired products.
# The inventory is listed on a given date.
#---------------------------------------------------------------------------------------------

def report_inventory(report_date):

    # Declare variables
    try:
        rep_date = datetime.strptime(report_date.strip("'"),'%Y-%m-%d')
    except:
        return 'ERROR, Wrong date format'

    # Create report header
    report_out = f'\n********** INVENTORY REPORT ON {report_date} **********'
    report_out += '\n+=============================+==========+=========+'
    report_out += '\n| Product Name                | In stock | Expired |'
    report_out += '\n+-----------------------------+----------+---------+'
    
    # Read products bought and create list with all products
    bought = {}
    products = set()
    f = open('bought.csv')
    reader = csv.reader(f)
    with f:
        for row in reader:
            product_id, product_name, buy_date, price, exp_date = row
            bought[product_id] = [product_name.replace("'", ""), buy_date, float(price), exp_date]
            if not product_name.replace("'", "") in products:
                products.add(product_name.replace("'", ""))
    
    # Read products sold and remove sold products from bought list
    f = open('sold.csv')
    reader = csv.reader(f)
    with f:
        for row in reader:
            product_id, sell_id, product_name, sold_date, price = row

            # Convert date to date objects for comparing
            sell_date = datetime.strptime(sold_date.strip("'"),'%Y-%m-%d')

            # If sell_date is before report_date, remove item from bought list
            if sell_date <= rep_date:
                if sell_id in bought:
                    del bought[sell_id]
    
    # Crystalize inventory from bought
    products_stock = {}
    products_expired = {}
    for key in bought:

        # Convert dates to date objects for comparing
        exp_date = datetime.strptime(bought[key][3].strip("'"),'%Y-%m-%d')
        buy_date = datetime.strptime(bought[key][1].strip("'"),'%Y-%m-%d')
        
        # Summarize products and expired products compared to report date 
        if buy_date <= rep_date:
            if exp_date >= rep_date:
                if bought[key][0] in products_stock.keys():
                   products_stock[bought[key][0]] += 1
                else:
                    products_stock[bought[key][0]] = 1
            else:
                if bought[key][0] in products_expired.keys():
                    products_expired[bought[key][0]] += 1
                else:
                    products_expired[bought[key][0]] = 1

    # Create report for all products bought
    for item in products:
        report_out += "\n| " + item.ljust(28) + "|" 
        if item in products_stock:
            report_out += str(products_stock[item]).center(10) + "|"
        else:
            report_out += str(0).center(10) + "|"
        if item in products_expired:
            report_out += str(products_expired[item]).center(9) + "|"
        else:
            report_out += str(0).center(9) + "|"

    report_out += '\n+=============================+==========+=========+'

    return report_out

def report_revenue(report_date):
    report_out = ''
    if report_date == str(date.today()): 
        report_out = "Today's revenue so far:"
    elif report_date == str(date.today()-timedelta(1)):
        report_out = "Yesterday's revenue:"
    else: 
        day = int(report_date.split('-')[2])
        month = int(report_date.split('-')[1])
        year = int(report_date.split('-')[0])
        report_out = 'Revenue from ' + date(year,month,day).strftime('%B ') + report_date.split('-')[0] + ':'
        print(report_out)
    return 'Ok'

def report_profit(date):
    pass

#---------------------------------------------------------------------------------------------
# Show report:
#---------------------------------------------------------------------------------------------
# Check which report has to be created:
# - inventory, shows inventory on certain date
# - revenue, shows revenue on certain date
# - profit, shows profit on certain date
#---------------------------------------------------------------------------------------------

def show_report(report_name, report_date):
    
    if report_name == 'inventory': return(report_inventory(report_date))
    elif report_name == 'revenue': return(report_revenue(report_date))
    elif report_name == 'profit': return(report_profit(report_date))
    
    # Non valid report name typed

    else:
        print(f"ERROR: unknown report '{report_name}' <inventory, revenue, profit>")
    return

def main():
    
    # Check report_inventory routine
    print(40 * '-' + '\nTesting inventory report:\n' + 40 * '-' + '\n')
    print('Test1: ', report_inventory('2021-01-01'))    # Right input
    print('Test2: ', report_inventory('2021-01-16'))    # Right input
    print('Test3: ', report_inventory('test'))          # Wrong input
    print('Test4: ', report_inventory(None))            # Wrong input
     
    return



if __name__ == '__main__':
    main()

import csv
from files import read_bought, read_sold
from datetime import date, timedelta, datetime

#---------------------------------------------------------------------------------------------
# Report inventory on certain date
#---------------------------------------------------------------------------------------------
# Return list with products in store and expired products.
# The inventory is listed on a given date.
#---------------------------------------------------------------------------------------------

def report_inventory(report_date):

    # Convert report date to date object
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
    bought = read_bought(report_date)
    productlist = set()
    for item in bought.items():
 
        # If product name not in product list, add it
        if not item[1][0] in productlist:  
            productlist.add(item[1][0])
     
    # Read products sold and remove sold products from bought list
    sold = read_sold(report_date)
    for item in sold.items():
        sell_date = datetime.strptime(item[1][1].strip("'"),'%Y-%m-%d')

        # If sell_date is before report_date, remove item from bought list
        if sell_date <= rep_date:
            if item[1][0] in bought:
                del bought[item[1][0]]

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
    for item in productlist:
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

# Revenue report, print revenue on a given date.

def report_revenue(report_date):

    # Check for montly revenue
    if len(report_date) != 10:
        return

    # Read products sold
    sold = read_sold(report_date)
    
    # Sumarize all prices in sold
    revenue = sum(item[1][3] for item in sold.items() )

    return 'Revenu on ' + report_date + ': EUR {:.2f}'.format(revenue)

def report_profit(report_date):

    # Check for montly revenue
    if len(report_date) != 10:
        return

    # Read products bought and sold on a given date
    bought = read_bought(report_date)
    sold = read_sold(report_date)
    
    # Sumarize all prices in bought
    total_bought = sum(item[1][2] for item in bought.items() )
    
    # Sumarize all prices in sold
    total_sold= sum(item[1][3] for item in sold.items() )
 
    return 'Profit on ' + report_date + ': EUR {:.2f}'.format(total_sold - total_bought)

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

    print('\nTest revenu:') 
    print(report_revenue('2021-01-01'))
    print(report_revenue('2021-01-04'))
    print(report_revenue('2021-01'))
  
    print('\nTest profit:') 
    print(report_profit('2021-01-01'))
    print(report_profit('2021-01-04'))
    print(report_profit('2021-01-08'))
    print(report_profit('2021-01'))

    return



if __name__ == '__main__':
    main()

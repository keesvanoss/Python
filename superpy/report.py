from datetime import date, timedelta

#---------------------------------------------------------------------------------------------
# Report inventory on certain date
#---------------------------------------------------------------------------------------------
# Return list with products, nr of products in store, buy price and expiration date.
# The inventory is listed until a given date.
#---------------------------------------------------------------------------------------------

def report_inventory(report_date):
      
# Create report
    report_out = ''
    report_out += '\n+--------------+-------+-----------+-----------------+'
    report_out += '\n| Product Name | Count | Buy Price | Expiration Date |'
    report_out += '\n+==============+=======+===========+=================+'
    
    print(report_out)
    return 'Ok'

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

if __name__ == '__main__':
    
    # Check report_inventory routine
    print('Test1: ', report_inventory('2021-03-26'))   # Right input
    print('Test2: ', report_inventory('test'))   # Wrong input
    
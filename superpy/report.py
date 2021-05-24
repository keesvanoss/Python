import csv
from files import read_bought, read_sold
from datetime import date, timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------------------------
# Report inventory on certain date
#---------------------------------------------------------------------------------------------
# Return list with products in store and expired products.
# The inventory is listed on a given date.
#---------------------------------------------------------------------------------------------

def report_inventory(report_date, exportcsv, showgraph):

    # Convert report date to date object
    try:
        rep_date = datetime.strptime(report_date.strip("'"),'%Y-%m-%d')
    except:
        return 'ERROR, Wrong date format'

    # Read products bought and create list with all products
    bought = read_bought(report_date)
    productlist = []
    for item in bought.items():
 
        # If product name not in product list, add it
        if not item[1][0] in productlist:  
            productlist.append(item[1][0])
     
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

    # Export inventory to REPORT.CSV
    if exportcsv == True:
        try:
            with open('report.csv', 'w') as export:
                export_writer = csv.writer(export, lineterminator = '\n')

                for item in productlist:
                    stock_out = products_stock[item] if item in products_stock else 0 
                    expired_out = products_expired[item] if item in products_expired else 0 
                    export_writer.writerow([item, stock_out, expired_out])
            return 'Data exported to REPORT.CSV'
        except:
            return 'ERROR, in creating datafile REPORT.CSV'
    if showgraph == True:

        # Show bar graph for inventory
        bars = list(productlist)
        values = []
        for key in bars:
            if key in products_stock:
                values.append(products_stock[key])
            else:     
                values.append(0)
        y_pos = np.arange(len(bars))
        plt.bar(y_pos, values)
        plt.xticks(y_pos, bars)
        plt.title('Inventory')
        plt.xlabel('Products')
        plt.ylabel('In stock')
        plt.show()
        return 'Inventory bar-graph showed'
    
    else:

        # Create inventory report
        report_out = f'\n********** INVENTORY REPORT ON {report_date} **********'
        report_out += '\n+=============================+==========+=========+'
        report_out += '\n| Product Name                | In stock | Expired |'
        report_out += '\n+-----------------------------+----------+---------+'
    
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

#---------------------------------------------------------------------------------------------
# Report all products bought before report-date
# --------------------------------------------------------------------------------------------

def report_products(report_date,exportcsv):

    # Convert report date to date object
    try:
        rep_date = datetime.strptime(report_date.strip("'"),'%Y-%m-%d')
    except:
        return 'ERROR, Wrong date format'

    bought = read_bought(report_date)
    productlist = set()
    for item in bought.items():
 
        # If product name not in product list, add it
        if not item[1][0] in productlist:  
            productlist.add(item[1][0])
    
    if exportcsv == True:
        # Export inventory to REPORT.CSV
        try:
            with open('report.csv', 'w') as export:
                export_writer = csv.writer(export, lineterminator = '\n')
                for item in productlist:
                    export_writer.writerow([item])
            return 'Data exported to REPORT.CSV'
        except:
            return 'ERROR, in creating datafile REPORT.CSV'
    else:
        # Create report 
        report_out = f'\nProducts available on {report_date}: '
        for item in productlist:
            report_out += item + ", "
        return report_out[:-2]
    endif

#---------------------------------------------------------------------------------------------
# Revenue report, print revenue on a given date.
#---------------------------------------------------------------------------------------------

def report_revenue(report_date, exportcsv):

    try:
        rep_date = datetime.strptime(report_date.strip("'"),'%Y-%m-%d')
    except:
        return 'ERROR, Wrong date format'

    # Check for montly revenue
    if len(report_date) != 10:
        return

    # Read products sold
    sold = read_sold(report_date)
    
    # Sumarize all prices in sold
    revenue = sum(item[1][3] for item in sold.items() )

    if exportcsv == True:
        # Export inventory to REPORT.CSV
        try:
            with open('report.csv', 'w') as export:
                export_writer = csv.writer(export, lineterminator = '\n')
                export_writer.writerow([revenue])
            return 'Data exported to REPORT.CSV'
        except:
            return 'ERROR, in creating datafile REPORT.CSV'
    else:
        # Create report 
        return '\nRevenu on ' + report_date + ': EUR {:.2f}'.format(revenue)

#---------------------------------------------------------------------------------------------
# Report profit on report-date
#---------------------------------------------------------------------------------------------

def report_profit(report_date, exportcsv):

    try:
        rep_date = datetime.strptime(report_date.strip("'"),'%Y-%m-%d')
    except:
        return 'ERROR, Wrong date format'

    # Read products bought and sold on a given date
    bought = read_bought(report_date)
    sold = read_sold(report_date)
    
    # Sumarize all prices in bought
    total_bought = sum(item[1][2] for item in bought.items() )
    
    # Sumarize all prices in sold
    total_sold= sum(item[1][3] for item in sold.items() )
 
    if exportcsv == True:
        # Export inventory to REPORT.CSV
        try:
            with open('report.csv', 'w') as export:
                export_writer = csv.writer(export, lineterminator = '\n')
                export_writer.writerow([round(total_sold - total_bought,2)])
            return 'Data exported to REPORT.CSV'
        except:
            return 'ERROR, in creating datafile REPORT.CSV'
    else:
        # Create report 
        return '\nProfit on ' + report_date + ': EUR {:.2f}'.format(total_sold - total_bought)

#---------------------------------------------------------------------------------------------
# Report products + info bought before report-date
#---------------------------------------------------------------------------------------------

def report_bought(report_date, exportcsv):

    # Convert report date to date object
    try:
        rep_date = datetime.strptime(report_date.strip("'"),'%Y-%m-%d')
    except:
        return 'ERROR, Wrong date format'
 
    # Read bought products 
    bought = read_bought(report_date)

    if exportcsv == True:
        # Export inventory to REPORT.CSV
        try:
            with open('report.csv', 'w') as export:
                export_writer = csv.writer(export, lineterminator = '\n')
                for key in bought:
                    name_out = bought[key][0]
                    buydate_out = bought[key][1] 
                    price_out = bought[key][2]
                    expdate_out = bought[key][3]
                    export_writer.writerow([name_out, buydate_out, price_out,expdate_out])
            return 'Data exported to REPORT.CSV'
        except:
            return 'ERROR, in creating datafile REPORT.CSV'
    else:     
        # Create report header
        report_out = f'\n************ BOUGHT REPORT ON {report_date} ***********'
        report_out += '\n+==============+============+=========+============+'
        report_out += '\n| Product Name |  Buy date  |  Price  |  Exp.date  |'
        report_out += '\n+--------------+------------+---------+------------+'

        # Create report for all products bought
        for key in bought:
            report_out += "\n| " + bought[key][0].ljust(13) + "|" 
            report_out += bought[key][1].replace("'", "").center(12) + "|" 
            report_out += "{:.2f}".format(bought[key][2]).center(9) + "|" 
            report_out += bought[key][3].replace("'", "").center(12) + "|" 
        report_out += '\n+==============+============+=========+============+'
        return report_out
 
#---------------------------------------------------------------------------------------------
# Report products + info sold or expired on report-date
#---------------------------------------------------------------------------------------------

def report_sold(report_date, exportcsv):

    # Convert report date to date object
    try:
        rep_date = datetime.strptime(report_date.strip("'"),'%Y-%m-%d')
    except:
        return 'ERROR, Wrong date format'
 
    # Read bought products 
    bought = read_bought(report_date)
    sold = read_sold(report_date)

    # Create report header
    report_out = f'\n******* SOLD + EXPIRED REPORT ON {report_date} ********'
    report_out += '\n+==============+============+=========+============+'
    report_out += '\n| Product Name |  Sold date |  Price  |  Exp.date  |'
    report_out += '\n+--------------+------------+---------+------------+'

    # Create report for all products sold and put ID in list
    soldlist = []

    if exportcsv == True:
        # Export inventory to REPORT.CSV
        try:
            with open('report.csv', 'w') as export:
                export_writer = csv.writer(export, lineterminator = '\n')
                for key in sold:
                    soldlist.append(sold[key[0]][0])
                    item = bought[sold[key[0]][0]]
                    export_writer.writerow(item)
                for key in bought:
                    if not key in soldlist:
                        exp_date = datetime.strptime(bought[key][3].strip("'"),'%Y-%m-%d')
                        if rep_date > exp_date:
                            item = [bought[key][0], 'Expired', '-', bought[key][3]]
                            export_writer.writerow(item)
            return 'Data exported to REPORT.CSV'
        except:
            return 'ERROR, in creating datafile REPORT.CSV'

    else:     
        for key in sold:
            soldlist.append(sold[key[0]][0])
            item = bought[sold[key[0]][0]]
            report_out += "\n| " + item[0].ljust(13) + "|" 
            report_out += sold[key][2].replace("'", "").center(12) + "|" 
            report_out += "{:.2f}".format(sold[key][3]).center(9) + "|" 
            report_out += item[3].replace("'", "").center(12) + "|" 
        report_out += '\n+==============+============+=========+============+'
    
        # Create report for all products expired
        sold_out = ''
        for key in bought:
            if not key in soldlist:
                exp_date = datetime.strptime(bought[key][3].strip("'"),'%Y-%m-%d')
                if rep_date > exp_date:
                    sold_out += "\n| " + bought[key][0].ljust(13) + "|" 
                    sold_out += 'Expired'.center(12) + "|" 
                    sold_out += '-'.center(9) + "|" 
                    sold_out += bought[key][3].replace("'", "").center(12) + "|" 
        if sold_out != '':
            report_out += sold_out
            report_out += '\n+==============+============+=========+============+'
        return report_out


#---------------------------------------------------------------------------------------------
# Show report:
#---------------------------------------------------------------------------------------------
# Check which report has to be created:
# - inventory, shows inventory on certain date
# - revenue, shows revenue on certain date
# - profit, shows profit on certain date
# - products, shows which products are available on certain date
# - bought, shows all products + info bought before a certain date
# - sold, shows all products + info sold or expired on a certain date
#---------------------------------------------------------------------------------------------

def show_report(report_name, report_date, export_csv, show_graph):
    
    # Check for valid report name typed
    if report_name == 'inventory': return(report_inventory(report_date, export_csv, show_graph))
    elif report_name == 'revenue': return(report_revenue(report_date, export_csv))
    elif report_name == 'profit': return(report_profit(report_date, export_csv))
    elif report_name == 'products':return(report_products(report_date, export_csv))
    elif report_name == 'bought':return(report_bought(report_date, export_csv))
    elif report_name == 'sold':return(report_sold(report_date, export_csv))
    else:
        print(f"ERROR: unknown report '{report_name}' <inventory, revenue, profit>")
    return

def main():
    
    # Check reports
    print(report_inventory('2021-01-03',False, True))
    print(report_sold('2021-01-11',True))
    print(report_products('2021-01-01',True))
    print(report_revenue('2021-01-01',False))
    print(report_profit('2023-09',False))
    print(report_profit('2021-01-01',False))
    print(report_profit('2023-09',False))
    print(report_bought('2021-01-01',False))
    print(report_sold('2021-01-11',False))
    return

if __name__ == '__main__':
    main()

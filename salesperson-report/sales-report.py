"""
sales_report.py - Generates sales report showing total number
            of melons each sales person sold.
"""

# initiates an empty dictionary for all melons sold
melon_orders = {}

# open file
f = open("sales-report.txt")

# iterate through file; format each line
for line in f:
    line = line.rstrip()
    entries = line.split("|")
    salesperson = entries[0]

    # checks if salesperson already in dictionary
    # if not, adds them & initiates empty lists for melons sold, order amts
    if melon_orders.get(salesperson, 0) == 0:
        melon_orders[salesperson] = {}
        melon_orders[salesperson]["Melons Sold"] = []
        melon_orders[salesperson]["Order Amounts"] = []
   
    # add each order amount & melon quantity to correct list
    melon_orders[salesperson]["Melons Sold"].append(int(entries[2]))
    melon_orders[salesperson]["Order Amounts"].append(float(entries[1]))


#print each salesperson's total melons sold
for salesperson in melon_orders.keys():
    print "{} : {} orders: {} melons sold; total sales = ${:.2f}.".format(
                            salesperson, 
                            len(melon_orders[salesperson].keys()),
                            sum(melon_orders[salesperson]["Melons Sold"]), 
                            sum(melon_orders[salesperson]["Order Amounts"])
                            )

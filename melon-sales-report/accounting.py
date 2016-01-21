
def count_melon_types_sold(orders):
    """ Reads sales records and counts melons of each type sold. """

    order_records = open(orders)
    melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}
    #iterate through order records
    for l in order_records:
        data = l.split("|")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count

    order_records.close()
    return melon_tallies

def total_melon_sales_by_type(melon_tallies):
    """ Reads melon_tallies output from count_melon_types_sold and calculates revenue from each type. """

    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold {} {} melons at ${:.2f} each for a total of ${:.2f}".format(melon_tallies[melon_type], melon_type, price, revenue)
    return ""

def tally_sales_by_channel(sales_records):
    """ Calculates total sales revenue for outbound vs internet sales from sales records. """
    
    sales_by_channel = open(sales_records)
    internet_sales = 0
    outbound_sales = 0
    #iterate through sales records
    for line in sales_by_channel:
        data = line.split("|")
        if data[1] == "0":
            internet_sales += float(data[3])
        else:
            outbound_sales += float(data[3])
    sales_by_channel.close()
    return [internet_sales, outbound_sales]
    

def compare_sales_channels(internet_sales, outbound_sales):
    """ Using the output of tally_sales_by_channel, compares sales channels. """

    print "Salespeople generated ${:.2f} in revenue.".format(outbound_sales)
    print "Internet sales generated ${:.2f} in revenue.".format(internet_sales)
    if outbound_sales > internet_sales:
        return "Guess there's some value to those salespeople after all."
    else:
        return "Time to fire the sales team! Online sales rule all!"


def sales_report_generator():
    """ Prints a formatted report in command line using other function outputs. """

    dorky_line_length = 80
    print "*" * dorky_line_length
    print "MELON SALES BY TYPE"
    print total_melon_sales_by_type(count_melon_types_sold("orders-by-type.txt"))
    print "*" * dorky_line_length
    print "MELON SALES BY CHANNEL"
    internet_sales, outbound_sales = tally_sales_by_channel("orders-with-sales.txt")
    print compare_sales_channels(internet_sales, outbound_sales)
    print "*" * dorky_line_length

sales_report_generator()
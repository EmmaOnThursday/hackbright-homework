def underpaying_customers(file_path):
    customer_data = open(file_path)
    for line in customer_data:
        line = line.rstrip()
        parsed_line = line.split("|")
        paid = float(parsed_line[3])
        owed = float(parsed_line[2])
        if owed > paid:
            print "{}: paid ${}; underpaid by ${}.".format(parsed_line[1], paid, (owed-paid))
    customer_data.close()

underpaying_customers("customer-orders.txt")
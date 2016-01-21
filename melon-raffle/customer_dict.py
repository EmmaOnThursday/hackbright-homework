def create_customer_dictionary(filepath):
    f = open('customers.txt')
    
    customers = {}

    for line in f:
        line = line.rstrip.split("|")
        customers[line[0]] = {"email": line[1], 
                        "street address": line[2],
                        "city" : line[3],
                        "zipcode" : line[4]}

    return customers

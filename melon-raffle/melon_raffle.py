from random import choice
from customer import Customer
from customer_info import *


def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    print "Contact {name} at {email} to notify them they've won".format(
        name = chosen_customer.name,
        email = chosen_customer.email
        )


pick_winner(customers)

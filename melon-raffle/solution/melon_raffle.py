from random import choice
from customer_info import organize_customer_data


def pick_winner(customers):
	"""Choose a random winner from list of customers and print contact info."""

	chosen_customer = choice(customers)

	print "Contact {name} at {email} to notify them they've won".format(
		name=chosen_customer.name,
		email=chosen_customer.email
		)


customers = organize_customer_data("customers.txt")

pick_winner(customers)


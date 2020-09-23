def list_to_str(list):
	return ','.join(str(elem) for elem in list)


def vikinglotto():
	import random

	row = [random.randint(1, 60) for _ in range(5)]
	additionals = [random.randint(1, 10), random.randint(1, 10)]

	# Convert to string
	str_row = list_to_str(row)
	str_additionals = list_to_str(additionals)

	return str_row, str_additionals

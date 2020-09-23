from vikinglotto import list_to_str, vikinglotto

num_of_rows = int(input('How many rows? '))
for _ in range(num_of_rows):
	row, additionals = vikinglotto()
	print(f'Output av vikingLotto: {row} tillägsnummer: {additionals}')

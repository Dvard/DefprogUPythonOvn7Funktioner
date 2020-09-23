import random


def random_char_from_string(text):
	return text[random.randint(0, len(text))].replace(' ', 'tom')


text = str(input('Text (minst 48 tecken) '))
if len(text) >= 48:
	print(random_char_from_string(text))


import random


def random_char_from_string(text):
	return text[random.randint(0, len(text))]


text = 'Vi gillar att koda python också på fritiden , och har lärt oss mycket på defprogu lektionerna :)'
print(random_char_from_string(text))

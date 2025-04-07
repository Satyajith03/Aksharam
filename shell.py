import aksharam

print('-'*100)
print("Namaskaram!")
print("Aksharam Bhaashayilekk Swagatham")
print('-'*100)

while True:
	text = input('aksharam> ')
	if text.strip() == "": continue
	result, error = aksharam.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
			
while True:
	message = input("Enter your message:")
	translate = ''
	i = len(message) - 1
	while i >= 0:
		translate = translate + message[i]
		i = i - 1
	print(translate)
	

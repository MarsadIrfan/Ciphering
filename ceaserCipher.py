message = input("Enter your message:")

key = int(input("Enter key:"))
while key > 25 or key < 0:
    print("Not a valid key (0-25)")
    key = int(input("Enter key:"))


mode = input("What do you want (encrypt or decrypt)????")

LETTERS =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        else:
            print("Please choose a valid option(encrypt or decrypt)")
            mode = input("What do you want (encrypt or decrypt)????")

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol


print(translated)
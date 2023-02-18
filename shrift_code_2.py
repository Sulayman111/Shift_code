alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
isWork = True
while isWork:
    print('1) Make a code\n2) Decode a message\n3) Quit')
    choice = int(input('Enter your selection: '))
    if choice == 1:
        txt = input('Enter your message: ')
        num = int(input('Enter a number (1-26): '))
        txt_low = txt.lower()
        mess = ''
        for letter in txt_low:
            position = alphabet.find(letter) 
            new_position = position + num
            if letter in alphabet:
                mess = mess + alphabet[new_position]
            else:
                mess = mess + letter
        print(mess)
        print('')
    elif choice == 2:
        txt = input('Enter your message: ')
        num = int(input('Enter a number (1-26): '))
        txt_low = txt.lower()
        mess = ''
        for letter in txt_low:
            position = alphabet.find(letter) 
            new_position = position - num
            if letter in alphabet:
                mess = mess + alphabet[new_position]
            else:
                mess = mess + letter
        print(mess)
        print('')
    elif choice == 3:
        isWork = False
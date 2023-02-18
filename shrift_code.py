alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
def get_data():
    word = input('Enter your message: ').lower()
    num = int(input('Enter a number (1-16): '))
    while num > 26 or num == 0:
        num = int(input('Out of range, Enter a number (1-16): '))
    data = (word, num)
    return data
def make_code(word, num):
    new_word = ""
    for i in word:
        j = alphabet.index(i)
        j += num
        if j > 26:
            j = j - 27
        char = alphabet[j]
        new_word = new_word + char
    print(f'shifr_code {word} -> {new_word}')
    print()
def decode(word, num):
    new_word = ""
    for i in word:
        j = alphabet.index(i)
        j -= num
        if j < 0:
            j = j + 27
        char = alphabet[j]
        new_word = new_word + char
    print(f'shifr_decode {word} -> {new_word}')
    print()
def main():
    isAgain = True
    while isAgain:
        print('1) Make a code')
        print('2) Decode a message')
        print('3) Quit')
        selection = input('Enter your selection: ')
        if selection == '1':
            (word, num) = get_data()
            make_code(word, num)
        elif selection =='2':
            (word, num) = get_data()
            decode(word, num)
        elif selection == '3':
            isAgain = False
        else:
            raise TypeError('your selection uncnown. Try again!')
if __name__ == '__main__':
    main()
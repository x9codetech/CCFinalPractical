word_dict = {
    'a': 'apple',
    'b': 'ball',
    'c': 'cat',
    'd': 'door'
}

letter = input("Enter a letter: ").lower()

if letter in word_dict:
    print(word_dict[letter])
else:
    print("You entered incorrectly.")

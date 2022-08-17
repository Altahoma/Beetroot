import random


word = input('Enter a word: ')
length = len(word)

for i in range(5):
    new_word = ''.join(random.sample(word, length))
    print(new_word)

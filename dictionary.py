import random


class Dictionary:

    def random_word(self):
        with open("dictionary.txt", "r", encoding="utf-8") as file:
            allText = file.read()
            word = list(map(str, allText.split()))
            return random.choice(word)


class Validator:

    def is_isogram(self, word):

        clean_word = self.lower_case(word)

        letter_list = []

        for letter in clean_word:
            if letter.isalpha():
                if letter in letter_list:
                    return False
                letter_list.append(letter)
        return True

    def lower_case(self, word):
        clean_word = word.lower()
        return clean_word

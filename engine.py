from dictionary import Dictionary
from validator import Validator
from stats import Stats

dictionary = Dictionary()
validator = Validator()
stats = Stats()
random_word = dictionary.random_word()


class Engine:
    word_from_user = ""
    def check_bulls_cows(self, word):
        i = 0
        stats.reset_cows()
        stats.reset_bulls()
        for x in word:
            if x in random_word:
                if x == random_word[i]:
                    stats.add_bulls()
                else:
                    stats.add_cows()
            i += 1

    def tworzenie_gry(self):
        print(f"Długość wylosowanego słowa to: {len(random_word)}")
        while True:
            while stats.chances > 0:
                word_from_user = input("Podaj slowo, ktore jest izogramem: ")
                self.check_bulls_cows(word_from_user)
                if not validator.is_isogram(random_word):
                    print("Słowo nie jest izogramem")
                if random_word == word_from_user:
                    print(f"Brawo! Udało ci się zgadnąć wylosowane słowo i zostało ci {stats.chances} szans")
                    break
                else:
                    stats.print_stats()
                    stats.chances -= 1
                    print("Nie traafiłeś! Spróbuj jeszcze raz")
                    print(f"Zostało ci {stats.chances} prób")
                    if stats.chances == 0:
                        print(f"Niestety ci się nie udało. Wylosowany izogram to: {random_word}")
            exit()

    def proby(self, trudnosc):
        stats.chances = trudnosc
        print(f"Masz teraz {trudnosc} prób")
        return trudnosc

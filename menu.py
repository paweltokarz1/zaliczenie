from engine import Engine

engine = Engine()


class Menu:
    menu_options = {
        1: "Nowa gra",
        2: "Zasady gry",
        3: "Zmień ilość prób",
        4: "Koniec",
    }

    def print_menu(self, menu_options):
        for key in menu_options.keys():
            print(key, '--', menu_options[key])
        return menu_options

    def nowa_gra(self):
        engine.tworzenie_gry()

    def zasady_gry(self):
        with open("zasady_gry.txt", "r", encoding="utf-8") as file:
            text = file.read()
        print(text)


    def zmien_ilosc_prob(self):
        ilosc = int(input('Wprowadź ilosc prób: '))
        engine.proby(ilosc)

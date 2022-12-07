from menu import Menu

menu = Menu()

while True:
    menu.print_menu(menu.menu_options)
    option = ''
    try:
        option = int(input('Wprowadź swój wybór: '))
    except:
        print('Niepoprawny input. Wpisz liczbę ...')
    if option == 1:
        menu.nowa_gra()
    elif option == 2:
        menu.zasady_gry()
    elif option == 3:
        menu.zmien_ilosc_prob()
    elif option == 4:
        print('Koniec gry')
        exit()
    else:
        print("Niepoprawna opcja. Podaj liczbe od 1 do 4.")

import random

owoce = [
    "jabłko", "banan", "granat",
    "gruszka", "ananas", "brzoskwinia",
    "nektarynka", "pitaja", "truskawka",
    "malina", "borówka", "jagoda", "kiwi",
    "pomarańcza", "grejfrut", "arbuz"]
imiona = [
    "bartosz", "katarzyna", "filip",
    "magdalena", "łukasz", "hanna",
    "marcin", "anna", "liliana",
    "barbara", "zenon", "andrzej",
    "radosław", "marek", "jędrzej", "adam"]
przyslowia = [
    "kto pod kim dołki kopie ten sam w nie wpada",
    "człowiek człowiekowi wilkiem",
    "niósł wilk razy kilka ponieśli i wilka",
    "kości zostały rzucone",
    "baba z wozu koniom lżej",
    "pies ogrodnika",
    "jak kuba bogu tak bóg kubie", ]

kategorie = {
    "owoce": owoce,
    "imiona": imiona,
    "przysłowia": przyslowia}


def wisielec(x):
    ksztalt = [[" ", " ", " ", " ", " ", " ", ],
               [" ", " ", " ", " ", " ", " ", ],
               [" ", " ", " ", " ", " ", " ", ],
               [" ", " ", " ", " ", " ", " ", ],
               [" ", " ", " ", " ", " ", " ", ],
               [" ", " ", " ", " ", " ", " ", ]]
    if x >= 1:
        ksztalt[5][0] = "_"
        ksztalt[5][1] = "_"
        if x >= 2:
            ksztalt[4][1] = "|"
            ksztalt[3][1] = "|"
            ksztalt[2][1] = "|"
            ksztalt[1][1] = "|"
            ksztalt[0][1] = "|"
            if x >= 3:
                ksztalt[0][2] = "-"
                ksztalt[0][3] = "-"
                if x >= 4:
                    ksztalt[0][4] = "|"
                    if x >= 5:
                        ksztalt[1][4] = "O"
                        if x >= 6:
                            ksztalt[2][4] = "|"
                            if x >= 7:
                                ksztalt[2][3] = "/"
                                if x >= 8:
                                    ksztalt[2][5] = chr(92)
                                    if x >= 9:
                                        ksztalt[3][4] = "^"
                                        ksztalt[4][3] = "/"
                                        if x >= 10:
                                            ksztalt[4][5] = chr(92)
    for element in ksztalt:
        for znak in element:
            print(znak, end=" ")
        print("")


def wisielec_game(kategorie):
    right_cathegory = False
    while right_cathegory != True:
        kategoria = input(f"podaj kategorię {list(kategorie.keys())} : ")
        try:
            haslo_male = random.choice(kategorie[kategoria])
            right_cathegory = True
        except:
            None
    haslo = haslo_male.upper()
    lista_liter_haslo = []
    for litera in haslo:
        lista_liter_haslo.append(litera)
    win = False
    podane_litery = []
    pozostale_pola = len(haslo)
    lista_do_planszy = []
    liczba_bledow = 0
    for lit in haslo:
        if lit == " ":
            znak = " "
        else:
            znak = "_"
        lista_do_planszy.append(znak)
        print(znak, end="")
    print("\n")
    while True:
        wybor = input(
            "wybierz czy chcesz zgadnąć hasło, czy podać literę."
            "Wpisz: litera/hasło. Wpisz l/h : ")
        if wybor == "l":
            right_letter = False
            litera = ""
            while right_letter != True or len(litera) != 1:
                litera = (input("podaj literę:")).upper()
                if len(litera) == 1:
                    try:
                        liczba = int(litera)
                    except ValueError:
                        right_letter = True
            if litera in podane_litery:
                print("ta litera już była sprawdzana")
            else:
                podane_litery.append(litera)
                if litera in haslo:
                    x = 0
                    while x < len(haslo):
                        if haslo[x] == litera:
                            lista_do_planszy[x] = litera
                            pozostale_pola -= 1
                        x += 1
                else:
                    liczba_bledow += 1
                    if liczba_bledow < 10:
                        print("tej litery nie ma w haśle, graj dalej")
                        wisielec(liczba_bledow)
                    elif liczba_bledow == 10:
                        wisielec(liczba_bledow)
                        print("przegrałeś!")
                        return
            print("")
            for lit in lista_do_planszy:
                print(lit, end="")
            print("")
            if pozostale_pola == 0:
                print("wygrana!")
                return
        elif wybor == "h":
            proba_uni = input("spróbój zgadnąć hasło: ")
            proba = proba_uni.upper()
            if proba == haslo:
                print(haslo)
                print("wygrana!")
                return
            else:
                liczba_bledow += 1
                if liczba_bledow < 10:
                    print("Niestety hasło jest inne. Graj dalej!")
                    wisielec(liczba_bledow)
                elif liczba_bledow == 10:
                    wisielec(liczba_bledow)
                    print("przerałeś!")
                    return


if __name__ == "__main__":
    wisielec_game(kategorie)

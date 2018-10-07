print('Goedendag!' '\n')
lees_kluizen = open('Kluizen.txt', 'r')
lees_kluizen_plus = open('Kluizen.txt', 'r+')
kluizen_append = open('Kluizen.txt', 'a')

def toon_aantal_kluizen_vrij():
    global lees_kluizen
    tel = 0
    resultaat = 12 - tel
    for regel in lees_kluizen.readlines():
        tel += 1
        resultaat = 12 - tel
    print('Het aantal beschikbare bagagekluizen is: {}'.format(resultaat))

def nieuwe_kluis():
    kluizen = list(range(1, 13))
    kluizen_nieuw = list(kluizen)
    global kluizen_append
    global lees_kluizen

    for regel in lees_kluizen.readlines():
        regel = regel.split(";")
        nummer = int(regel[0])
        kluizen_nieuw.remove(nummer)
        lees_kluizen.close()

    if len(kluizen_nieuw) == 0:
        print("Er zijn geen kluisjes vrij!")
    else:
        wachtwoord = str(input("Voer een nieuw wachtwoord voor uw kluis in:"))
        if len(wachtwoord) < 4:
            print("Het wachtwoord is niet lang genoeg!"'\n'
                  'Voer een nieuw wachtwoord in''\n')
        else:
            kluizen_append.write('\n''{};{}'.format(min(kluizen_nieuw), wachtwoord))
            print("Gelukt! Uw nieuwe kluis heeft nummer: ", min(kluizen_nieuw))
            kluizen_append.close()

def kluis_openen():
    kluis = str(input("Voer uw kluisnummer in:"))
    wachtwoord = str(input("Voer uw wachtwoord in:"))
    global lees_kluizen

    for regel in lees_kluizen.readlines():
        regel = regel.split(";")
        nummer = str(regel[0])
        ww = str(regel[1])
        lees_kluizen.close()
        if nummer == kluis and ww == (wachtwoord):
            print("Gegevens zijn juist, uw kluisje is open!")
            break
        elif nummer == kluis and ww != (wachtwoord):
            print("Het wachtwoord is onjuist!")
            break
    else:
        print("Ingevoerde kluisje ontbreekt in database!")

def kluis_teruggeven():
    kluisje = str(input("Voer uw kluisnummer in:"))
    wachtwoord = str(input("Voer uw wachtwoord in:"))
    global lees_kluizen

    for lijn in lees_kluizen.readlines():
        lijn = lijn.split(";")
        nummer = str(lijn[0])
        ww = str(lijn[1])
        lees_kluizen.close()
        if nummer == kluisje and ww ==(wachtwoord):
            regel = kluisje + ';' + wachtwoord
            lijn_verwijderd = 0
            global lees_kluizen_plus
            lijnen = lees_kluizen_plus.readlines()
            lees_kluizen_plus.seek(0)
            for lijn in lijnen:
                if not lijn.startswith(str(regel)):
                    lees_kluizen_plus.write(lijn)
                else:
                    print("Het verwijderen van kluisnummer", kluisje, "is gelukt!")
                    lijn_verwijderd += 1
            lees_kluizen_plus.truncate()
            lees_kluizen_plus.close()
            break
        elif nummer == kluisje and ww != (wachtwoord + '\n'):
            print("Het wachtwoord is onjuist!")
            break
    else:
        print("Ingevoerde kluisje ontbreekt in database!")

def menu():
    print('\n''1: Ik wil weten hoeveel kluizen nog vrij zijn' '\n'
    '2: Ik wil een nieuwe kluis''\n'
    '3: Ik wil even iets uit mijn kluis halen''\n'
    '4: Ik geef mijn kluis terug' '\n')

    keuze= (input("Geef een keuze op." '\n'))
    if keuze.isdigit():
        keuze = int(keuze)
        if keuze == 1:
            toon_aantal_kluizen_vrij()
        elif keuze == 2:
            nieuwe_kluis()
        elif keuze == 3:
            kluis_openen()
        elif keuze == 4:
            kluis_teruggeven()
        else:
            print('Dat antwoord herken ik niet! Wil je alsjeblieft een nummer invoeren die ik wel ken? (1 t/m 4)' '\n')
            menu()
    else:
        print('Dat antwoord herken ik niet! Wil je alsjeblieft een nummer invoeren die ik wel ken? (1 t/m 4)' '\n')
        menu()
menu()
print('\n''Deze code draait maar 1 keer vanwege I/O close-problemen: I/O operation on closed file''\n'
      "Om andere dingen te doen, moet je de code herstarten."'\n''\n')
print('Tot ziens!')
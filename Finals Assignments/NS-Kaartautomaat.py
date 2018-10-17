import datetime
import locale
locale.setlocale(locale.LC_ALL, "nl_NL")

def tijd():
    vandaag = datetime.datetime.today()
    s = str(vandaag.strftime("%A %d %B %Y." '\n' 
        'De tijd is ' + "%T." '\n' '\n'))
    return(s)
print("Goedendag!" '\n'
      'het is vandaag ' + tijd())
print("Welkom bij de NS Kaartautomaat!")
def inlezen_beginstation(stations):
    begin = str(input("Voer een beginstation in:"))
    while begin not in stations:
        print("Dit station bestaat niet.")
        begin = str(input("Voer een beginstation in:"))
    if begin == stations[-1]:
        print(begin + ' is het eindstation!')
        exit()
    else:
        print("Invoer OK!")
        return begin

def inlezen_eindstation(stations, beginstation):
    eind = input("Voer een eindstation in:")

    while eind not in stations:
        print("Of dit station bestaat niet, of deze trein gaat niet naar " + eind +", of je hebt het station verkeerd ingetypt.")
        eind = input("Voer een eindstation in:")

    while stations.index(eind) <= stations.index(beginstation):
        print("Dit kan niet! Je heb de volgorde verkeerd, of je hebt hetzelfde eindstation ingevoerd.")
        eind = input("Voer een eindstation in:")
        while eind not in stations:
            print("Of dit station bestaat niet, of deze trein gaat niet naar " + eind +", of je hebt het station verkeerd ingetypt.")
            eind = input("Voer een eindstation in:")
    print("Invoer OK!")
    return eind

def omroepen_reis(stations, beginstation, eindstation):
    print("Het beginstation {} is het {}e station in het traject".format(beginstation, stations.index(beginstation) + 1 ))
    print("Het eindstation {} is het {}e station in het traject".format(eindstation, stations.index(eindstation) + 1 ))
    print("De afstand bedraagt {} station(s)".format((stations.index(eindstation) + 1) - (stations.index(beginstation) + 1)))
    print("De prijs van het kaartje is {} euro".format(((stations.index(eindstation) + 1) - (stations.index(beginstation) + 1))*5))
    print("")
    print("Je stapt in bij:",beginstation)
    for i in stations[stations.index(beginstation) + 1:stations.index(eindstation)]:
        print("\tVolgende station:","-", i, end="\n")
    print("Je stapt uit bij:", eindstation)

print('Ik heb 2 trajecten in de test staan:' '\n'
      '1: Traject Schagen - Maastricht' '\n'
      '2: Traject sprinter Dordrecht - Arnhem Centraal')
try:
    keuze = int(input("Wat is uw keuze? Voer alleen 1 of 2 in, anders stopt het programma!" '\n'))
except ValueError:
    print('Ik had je toch gewaarschuwd! >:(')
    exit()
if keuze==1:
    stations = ['Schagen', 'Heerhugowaard','Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
elif keuze==2:
    stations = ['Dordrecht', 'Dordrecht Zuid','Lage Zwaluwe', 'Breda-Pinsenbeek', 'Breda', 'Gilze-Rijen', 'Tilburg Reeshof', 'Tilburg Universiteit', 'Tilburg', "'s-Hertogenbosch", '’s-Hertogenbosch Oost', 'Rosmalen', 'Oss West', 'Oss', 'Ravenstein','Wijchen', 'Nijmegen Dukenburg', 'Nijmegen Goffert', 'Nijmegen', 'Nijmegen Lent', 'Elst', 'Arnhem Zuid', 'Arnhem Centraal']
else:
    print('Ik had je toch gewaarschuwd! >:(')
    exit()
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
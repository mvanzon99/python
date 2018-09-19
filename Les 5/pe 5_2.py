leeftijd = (input("Geef je leeftijd: "))
leeftijd = int(leeftijd)
paspoort = (input("Heb je een Nederlands paspoort? ja / nee: "))
if leeftijd >= 18 and paspoort == "ja" :
    print("Gefeliciteerd, je mag stemmen!")
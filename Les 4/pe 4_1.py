cijferICOR = 6.0
cijferPROG = 7.5
cijferCSN = 8.0

gemiddelde = (cijferCSN + cijferPROG + cijferICOR) /3
gemiddelde =(round(gemiddelde, 1))
beloning = (gemiddelde / 0.1 * 3)
beloning = int(beloning)
beloning= str(beloning)
gemiddelde = str(gemiddelde)

overzicht = "Mijn cijfers (gemiddeld een " + gemiddelde +") leveren een beloning van €" + beloning + " op!"

print(overzicht)
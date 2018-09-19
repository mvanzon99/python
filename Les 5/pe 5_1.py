score = (input("Geef je score: "))
score = int(score)

if score >15:
    print("Gefeliciteerd!")
    print("Met een score van " + str(score) + " ben je geslaagd!")
else:
    print("Helaas!")
    print("Met een score van " + str(score) + " ben je helaas gezakt.")
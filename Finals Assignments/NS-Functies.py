def standaardtarief(afstandKM):
    if afstandKM >= 50:
        tarief = afstandKM * 0.60 + 15
    elif afstandKM < 0:
        return 0
    else:
        tarief = afstandKM * 0.80
    return tarief

def ritprijs(leeftijd, weekendrit, afstandKM):
    tarief = standaardtarief(afstandKM)
    if leeftijd >= 65 or leeftijd < 12:
        if weekendrit == True:
            tarief = tarief / 100 * 65
        else:
            tarief = tarief / 100 * 70
    elif weekendrit == True:
        tarief = tarief / 100 * 60
    else:
        return tarief
    return round(tarief, 2)

# 1: An 11-year-old travels 65 kilometres on a weekday.
print(ritprijs(11, False, 65))

# 2: A 64-year-old travels 38 kilometres on the weekend.
print(ritprijs(64, True, 38))

# 3: A 35-year-old travels 125 kilometres on a weekday.
print(ritprijs(35, False, 125))

# 4: A 9-year-old travels 49 kilometres on the weekend.
print(ritprijs(9, True, 49))

# 5: A 50-year-old travels 170 kilometres on the weekend.
print(ritprijs(50, True, 170))

#6: A 7-year-old travels 35 kilometres on the weekend.
print(ritprijs(7, True, 35))

#7: A 5-year-old travels 20 kilomtres on a weekday.
print(ritprijs(5, False, 20))

#8: An 80-year-old travels 225 kilometres on a weekday.
print(ritprijs(80, False, 225))

#9: Negative test
print(ritprijs(15, False, -6))
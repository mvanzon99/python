grondgetallen = [4, 5, 3, -81]
def kwadraten_som(grondgetallen):
    positief = []
    for x in grondgetallen:
        if x >= 0:
            x = x * x
            positief.append(x)
    return sum(positief)


print(kwadraten_som(grondgetallen))
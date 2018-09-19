s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = list("aeoiu")

for x in list(s):
    if x in klinkers:
        print(x, end='')
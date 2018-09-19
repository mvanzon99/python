def lang_genoeg(lengte):
    if lengte >= 120:
        return("Je bent lang genoeg voor de attractie!")
    elif lengte < 120:
        return("Sorry, je bent te klein!")

print(lang_genoeg(120))
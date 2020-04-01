def calculateWeight(mass, planet = "Earth", gravity = 9.807):
    weight = round(mass*gravity, 2)
    return "A " + str(mass) + " kg object weighs "+ str(weight) + " Newtons on " + planet + "."


print(calculateWeight(10.0))
print(calculateWeight(5.0, planet="Jupiter", gravity=24.79))

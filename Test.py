import random as rand

randNumber = rand.randint(0,100)

if randNumber < 20:
    print("Mini")
elif randNumber > 20 and randNumber < 50:
    print("Medium")
else:
    print("Large")
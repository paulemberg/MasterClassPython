parrot = "Norwegian Blue"

letter = input("Enter a character")

if letter not in parrot:
    print("I don't need that letter")
else:
    print("Gibe me an {}, Bob".format(letter))

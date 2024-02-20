print("🎲🎲 Roll it 13 🎲🎲")


# loop for testing purposes

while True:
    want_instructions = input("do you want to read the instructions?").lower()

    if want_instructions == "yes":
        print("you chose yes")
    elif want_instructions == "y":
        print("you chose yes")
    elif want_instructions == "no":
        print("you chose no")
    elif want_instructions == "n":
        print("you chose no")
    else:
        print("you did not choose a valid response")


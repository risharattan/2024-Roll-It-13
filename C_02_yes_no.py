# checks user enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes":
            return "yes"
        elif response == "no":
            return "no"
        else:
            print("you did not choose a valid response")






# Main routine
    want_instructions = yes_no("do you want to read the instructions? ")
    print(f"you chose {want_instructions}")


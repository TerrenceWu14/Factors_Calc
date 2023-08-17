# Functions go here

# Puts series of symbols at the start and end of the text (for emphasis)
def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Instructions for how to use the calculator
def instructions():
    statement_generator("Instructions / Information", "=")
    print()
    print(" Please only type a number between 1 to 200 (with no decimals)")
    print("Complete as many calculations as necessary, "
          "pressing <enter> at the end of each calculator or any key to quit.")
    print()
    return ""


# Checks that the number is equal to or below 200
def num_check(question1: object):
    # checks if the user entered a number that is more than zero
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero and lower (or equal to) than 200 (no decimals)"

        try:

            # asks user to enter a number
            response = int(input(question1))

            # checks if a number is above zero
            if 0 < response <= 200:
                return response

            # Outputs error if number is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Main routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Displays instruction / information
first_time = input("Press <enter> for instructions if it's your first time using this calculator otherwise any other "
                   "key to skip")
if first_time == "":
    instructions()

question = "Please enter a number that is more than zero and lower (or equal to) than 200 (no decimals)"

keep_going = ""
while keep_going == "":
    comment = ""

    to_factor = num_check(question)
    factor_list = []

    if to_factor == 1:
        print("One is unity! It only has one factor and that is itself.")
        factor_list.append(1)
    else:
        # Finds factors and returns sorted list
        sqrt_to_factor = int(to_factor ** 0.5)
        for item in range(1, sqrt_to_factor + 1):
            remainder = to_factor % item
            possible_factor = to_factor // item
            if remainder == 0:
                # add factor to list
                factor_list.append(item)
                if item != to_factor // item:
                    factor_list.append(to_factor // item)
                factor_list.sort()

    print()
    # print("Factors: ", factor_list)
    print(f"👀👀👀 Factors of {to_factor} 👀👀👀")
    # checks if the number is a perfect square or a prime number
    if len(factor_list) % 2 == 1 and to_factor != 1:
        print(f"{to_factor} is a perfect square! 🟧")
    elif len(factor_list) == 2:
        print(f"{to_factor} is a prime number! ")
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()

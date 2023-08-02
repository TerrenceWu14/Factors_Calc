# Functions go here

# Instructions for how to use the calculator
def instructions():
    statement_generator("Instructions / Information", "=")
    print()
    print(" Please type a number between 1 to 200 (with no decimals)")
    print()
    print("This program assumes that images are being represented in 24 bit color (ie: 24 bits per pixel). "
          "For text we assume that ascii encoding is being used (8 bits per character)")
    print()
    print("Complete as many calculations as necessary, "
          "pressing <enter> at the end of each calculator or any key to quit.")
    print()
    return ""


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


# Checks input is a number more than a given value
def num_check(question):
    # checks if the user entered a number that is more than zero
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero and lower (or equal to) than 200"

        try:

            # asks user to enter a number
            response = float(input(question))

            # checks if a number is above zero
            if 0 < response <= 200:
                return response

            # Outputs error if number is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Gets factors, returns a sorted list
def get_factors(to_factor):


# Main Routine

# Heading
statement_generator("Factors Calculator", "-")

# Displays instruction / information
first_time = input("Press <enter> for instructions if it's your first time using this calculator otherwise any other "
                   "key to skip")
if first_time == "":
    instructions()

# Loops to allow for multiple calculations per session
keep_going = ""
while keep_going == "":
    comment = ""

    # Asks the user for the number
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factors_list = ""
        comment = "One is unity! It only has one factor and that is itself."

    # Comments for squares / primes
    if len(factors_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factors_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # Outputs factors and comment

    # Generate heading
    if var_to_factor == 1:
        heading = "One is special"
    else:
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factors_list)
    print()

    print()
    keep_going = input(" Press <enter> to continue or any key to quit ")
    print()

    print()
    print("Thank you for using the factors calculator")
    print()

def num_check(question):
    # checks if the user entered a number that is more than zero
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero and lower (or equal to) than 200 (no decimals)"

        try:

            # asks user to enter a number
            response = int(input(question))

            # checks if a number is above zero
            if 0 < response <= 200:
                return response

            # Outputs error if number is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


question = "Please enter a number that is more than zero and lower (or equal to) than 200 (no decimals)"
to_factor = int(input(question))
factor_list = []

for item in range(1, to_factor + 1):
    print(item)
    remainder = to_factor % item
    possible_factor = to_factor // item

    print("possible", possible_factor)
    print("remainder", remainder)

    if remainder == 0:
        print("WE have a winner!!")

        # add factor to list
        factor_list.append(possible_factor)

factor_list.sort()
print("Factors: ", factor_list)

def num_check(question):
    # Checks if the user entered a positive integer between 1 and 200
    while True:
        try:
            response = int(input(question))
            if 1 <= response <= 200:
                return response
            else:
                print("Please enter a number between 1 and 200 (inclusive).")
        except ValueError:
            print("Please enter a valid integer.")

# Get a valid number from the user
question = "Please enter a number that is more than zero and lower (or equal to) than 200 (no decimals): "
to_factor = num_check(question)
factor_list = []

# Only check factors up to the square root of the given number
sqrt_to_factor = int(to_factor ** 0.5)

for item in range(1, sqrt_to_factor + 1):
    remainder = to_factor % item
    possible_factor = to_factor // item

    if remainder == 0:
        # Add factor to list
        factor_list.append(item)
        # Avoid adding the same factor twice for non-perfect squares
        if item != possible_factor:
            factor_list.append(possible_factor)

factor_list.sort()
print("Factors:", factor_list)






# Modulo example

keep_going = ""
while keep_going == "":

    num_lollies = int(input("How many lollies? "))
    num_students = int(input("How many students? "))

    # Lollies per student (divide)
    lollies_per_student = num_lollies // num_students
    lollies_left = num_lollies % num_students

    # Output fixer (lolly vs lollies)
    if lollies_left == 1:
        lolly_pl = "lolly"
    else:
        lolly_pl = "lollies"

    # Output...
    print()
    print(" You have {} lollies and {} students"
          .format(num_lollies, num_students))
    print()
    keep_going = input(" Press <enter> to continue or any key to quit ")
    print()

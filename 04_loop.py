

# rounds loop starts here
end_game = "no"
while rounds_played < rounds and end_game == "no":

    # checks if mode is regular or infinite and creates heading
    if mode == "infinite":
        heading = "----- Round {} -----".format(rounds_played + 1)
        rounds += 1
    else:
        heading = "----- Round {} of {} ------".format(rounds_played + 1, rounds)

    # prints heading
    print()
    print(heading)

    # Generates random number within the range given by the user
    n1 = random.randint(low_num, high_num)
    n2 = random.randint(low_num, high_num)

    # Print question using correct operation
    if operation == 1:
        print()
        print("{} + {} = ".format(n1, n2))

    elif operation == 2:
        print()
        print("{} x {} = ".format(n1, n2))

    # Asks for the answer
    # Checks if answer is correct or incorrect based on operation chosen by the user
    ans = intcheck("Answer: ", exit_code="xxx")

    if ans == "xxx":
        print()
        print("!!!You quit the game!!!")
        break

    if operation == 1:
        operation_symbol = "Addition(+)"
        if ans == (n1 + n2):
            print()
            print("!!!!!You Got It!!!!!")
            rounds_won += 1
        else:
            print()
            print("***Incorrect***")
            print("The correct answer was {}".format(n1 + n2))
            rounds_lost += 1

    if operation == 2:
        operation_symbol = "multiplication(x)"
        if ans == (n1 * n2):
            print()
            print("!!!!!You Got It!!!!!")
            rounds_won += 1

        else:
            print()
            print("***Incorrect***")
            print("The correct answer was {}".format(n1 * n2))
            rounds_lost += 1
    # Rounds played increases by one
    rounds_played += 1
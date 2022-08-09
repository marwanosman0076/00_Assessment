import random


# Ask user if they have played before
def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = '{} {} {}'.format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""


# Yes No Function
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return "yes"

        elif response == 'no' or response == 'n':
            return "no"
        else:
            print('please answer yes / no\n')


# Instructions def
def instructions():
    print()
    print('**** How To Play ****')
    print(
        """The aim of this game is simple. Choose an amount of rounds that you would like to play.Then insert your range of numbers.
You will then be given a basic fact question using the range you inserted to answer. Your score will be displayed at the end.
If at any time you wish to exit the game, type xxx. Good Luck!!"""
    )
    print()
    return ''


# Number checking function goes here
def intcheck(question, low=None, high=None, exit_code=None):
    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(
                low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(
                low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(
                high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)

            # check to see if response is the exit code and return it
            if response == exit_code:
                return response

            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print()
            print(error)
            continue

# Statement generator
print()
statement_generator("Welcome to Basic Facts", "*")

print()


# Makes sure that the asnwer to the played before question is either yes, y, no, n using yes_no checker
played_before = yes_no('Have you played this game before? ')


# checking if user have played before
if played_before == 'no':
    print()
    instructions()


# Resets rounds played, rounds lost and rounds won before the game
rounds_played = 0
rounds_won = 0
rounds_lost = 0


# Mode is regular
mode = "regular"


# Asks user for number of rounds to play or enter for infinite mode
rounds = intcheck("How many rounds do you want to play (Press enter for infinite mode):", 1, exit_code="")


# Ask user for the operation they want to use while checking the answer is either 1 or 2
print()
print("Choose your operator")
operation = intcheck("Addition-1     Multiplication-2  : ", low=1, high=2)


# user enters range of numbers here
print()
low_num = intcheck("Enter the Lowest number: ", low=0)
print()
high_num = intcheck("Enter Highest number: ", low=low_num)

# if user presses enter, mode becomes infinite
if rounds == "":
    mode = "infinite"
    rounds = 10


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


# ***** calculate game stats *****
# if rounds played is zero, print "You have no game history" else:
# Create percentages of games won/games lost based on rounds won/rounds lost divided by rounds played times 100
if rounds_played == 0:
    print()
    print("You have no game history")
else:
    percent_win = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    print()

    # displays game stats with % values to the nearest whole number
    print("***** Game Statistics *****")
    print(
        "Correct: {}, ({:.0f}%)\nIncorrect: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lost, ))

    # end of game statements
    print()
    print("***** END GAME SUMMARY *****")
    print()
    print("You choose {} as your operator".format(operation_symbol))
    print()
    print("You played {} rounds".format(rounds_played))
    print()
    print("Correct: {} \t\t Incorrect: {}".format(rounds_won, rounds_lost))

print()
print("!!!Thanks for playing!!!")



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
            print('please answer yes / no')


def instructions():
    print()
    print('**** How To Play ****')
    print("""The aim of this game is simple. Choose an amount of rounds that you would like to play. Then insert your
range of numbers. You will then be given a basic fact question using the range you inserted to answer . Your
score will be displayed at the end.""")
    print()
    return ''
print()
statement_generator("Welcome to Basic Facts", "*")
print()

played_before = yes_no('have you played the game before? ')

if played_before == 'no':
    instructions()
else:
    print("Program Continues")


# Number checking function goes here

def intcheck(question, low=None, high=None, exit_code=None):
    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
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
            print(error)
            continue

# User chooses mode

rounds_played = 0

mode = "regular"

rounds = intcheck("How many rounds do you want to play (Press enter for infinite mode):", 1, exit_code="")
if rounds == "":
    mode = "infinite"
    rounds = 100000000000000000

# user enters range of numbers here

low_num = intcheck("Enter the lowest number: ", low=0)

high_num = intcheck("Enter Highest number: ", low=low_num)


# rounds loop starts here
end_game = "no"
while rounds_played < rounds and end_game == "no":

    if mode == "infinite":
        heading = "----- Round {} -----".format(rounds_played + 1)
    else:
        heading = "----- Round {} of {} ------".format(rounds_played + 1, rounds)

    rounds_played += 1

    print()
    print(heading)

    # Generates random number within the range given by the user

    n1 = random.randint(low_num, high_num)
    n2 = random.randint(low_num, high_num)

    # Print question

    print("{} + {} = ".format(n1, n2))

    # Asks for the answer
    # Checks if answer is correct or incorrect

    ans = intcheck("Answer: ")

    if ans =="xxx":
        break

    if ans == (n1 + n2):
        print()
        print("!!!!!You Got It!!!!!")

    else:
        print("***Incorrect***")








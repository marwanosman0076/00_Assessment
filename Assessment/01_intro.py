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
print("Welcome to Basic Facts")
print()

played_before = yes_no('have you played the game before? ')

if played_before == 'no':
    instructions()
else:
    print("Program Continues")

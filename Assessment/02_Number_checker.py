import random

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

# user enters range of numbers here

low_num = intcheck("Enter the lowest number: ", low=0)

high_num = intcheck("Enter Highest number: ", low=low_num)

# Generates random number within the range given by the user

n1 = random. randint(low_num, high_num)
n2 = random. randint(low_num, high_num)

# Print question
print("{} + {} = ".format(n1, n2))


# Asks for the answer
# Checks if answer is correct or incorrect

ans = intcheck("What is the answer: ")

if ans == (n1 + n2):
    print("Correct")

else:
    print("incorrect")




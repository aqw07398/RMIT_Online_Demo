import sys

def main():

    ''' main function starts here '''

    menu = "\n-----------\n"
    menu += "1. Addition \n"
    menu += "2. Subtraction \n"
    menu += "3. Close \n"
    menu += "\n-----------\n"

    counter = 0

    sys.stdout.write(menu)

    answer = int(sys.stdin.readline())

    while (answer != 3):

        if (answer == 1):
            counter += 1

        elif (answer == 2):
            counter -= 1

        sys.stdout.write("\nCounter: " + str(counter))

        sys.stdout.write(menu)

        answer = int(sys.stdin.readline())

    sys.stdout.write("\nOut!")



main()

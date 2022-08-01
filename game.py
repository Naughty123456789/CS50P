import random
import sys


def main():
    while True:
        try:
            n=int(input("Level:").strip())

            if n>=1:
                break
        except ValueError:
            print("Not an integer")
            pass
    generated_number= random.randint(1,n)

    while True:
        try:
            guess3=input("Guess:").strip()


            if guess3.isalpha():
                print("Not an integer")
                sys.exit(1)
            guess=int(guess3)
            if guess<1:
                print("Not a positive integer")
                sys.exit(2)

        except ValueError:
            print("Not an integer")
            pass



        if guess<generated_number:
            print("Too small!")
        if guess>generated_number:
            print("Too large!")

        if guess==generated_number:
            print("Just right!")
            break





main()
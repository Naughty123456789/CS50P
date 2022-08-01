import random


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


            guess=int(input("Guess:").strip())

            if guess<1:
                print(4/0)

            if guess<generated_number:
                print("Too small!")
            if guess>generated_number:
                print("Too large!")

            if guess==generated_number:
                print("Just right!")
                break

        except (ValueError, UnboundLocalError):
            print("Not an integer")
            pass

        except ZeroDivisionError:
            print("Not a positive integer")
            pass






main()
from validator_collection import validators
def main():
    x=input("What is your email:").strip()
    print(checking(x))




def checking(s):


    try:

        x=validators.email(s)
        return "Valid"

    except ValueError:

        return "Invalid"









if __name__ == "__main__":
    main()
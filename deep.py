def main():
    user=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

    if user =="42" or user =="forty-two" or user =="forty two":
        print("Yes")

    else:
        print("No")



main()
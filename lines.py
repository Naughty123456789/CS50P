import sys


def main():
    try:
        checking_command()
        file=open(sys.argv[1], "r")
        read_file=file.readlines()
        num=0
        for row in read_file:
            if not row.strip().startswith("#") and row.strip() !='':
                num+=1


        print(num)

    except FileNotFoundError:
        print("File not found ")
        sys.exit(1)

def checking_command():
    if len(sys.argv)>2:
        print("Too many command-line arguements")
        sys.exit(1)
    if len(sys.argv)<2:
        print("Too few command-line arguements")
        sys.exit(1)
    elif ".py" not in  sys.argv[1]:
        print("Not a python file")
        sys.exit(1)




if __name__ == "__main__":
    main()



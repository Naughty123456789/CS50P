import sys
from tabulate import tabulate
import csv


def main():
    table=[]
    checking_command_line()

    try:
        with open(sys.argv[1], "r") as file:
            new_file=csv.reader(file)

            for row in new_file:
                table.append(row)

        print(table[0])
        print(tabulate(table[1:],headers=table[0],tablefmt="grid"))

    except FileNotFoundError:
        print("File not found")








def checking_command_line():

    if len(sys.argv)>2:
        print("Too many command-line arguements")
        sys.exit(1)
    if len(sys.argv)<2:
        print("Too few command-line arguements")
        sys.exit(1)
    elif ".csv" not in sys.argv[1]:
        print("Wrong File")
        sys.exit(1)


if __name__ == "__main__":
    main()







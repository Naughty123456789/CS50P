import csv
import sys


def main():
    try:
        checking_command_line()
        with open(sys.argv[1],"r") as file:
            new_file= csv.DictReader(file)
            d=[]
            for row in new_file:
                last,first=row["name"].split(", ")
                d.append({'first': first.lstrip(),"last":last, "house":row["house"]} )


         

            with open(sys.argv[2],"w") as file2:
                fieldname=["first","last","house"]
                writer=csv.DictWriter(file2, fieldnames=fieldname)
                writer.writerow({"first":"first","last": "last","house":"house"})
                for i in d:
                    writer.writerow({"first": i["first"],"last": i["last"],"house": i["house"]})

    except FileNotFoundError:
        print("File not found")
        sys,exit(1)




def checking_command_line():
    try:
        if len(sys.argv)>3:
            print("Too many command-line arguements")
            sys.exit(1)
        if len(sys.argv)<3:
            print("Too few command-line arguements")
            sys.exit(1)
        elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
            print("Wrong File")
            sys.exit(1)

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)



if __name__ == "__main__":
    main()
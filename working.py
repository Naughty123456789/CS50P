import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

        correct_format= re.search(r"^([0-9][0-2]*)(:)*([0-5][0-9])* (AM|PM) to ([0-9]{1}[0-2]*)(:)*([0-5][0-9])* (AM|PM)$",s)
        if correct_format:
            pieces=correct_format.groups()


            if int(pieces[0])>12 or int(pieces[4])>12:
                raise ValueError

            first_part=new_format(pieces[0],pieces[2],pieces[3])
            second_part=new_format(pieces[4],pieces[6],pieces[7])

            return first_part + " to " + second_part

        else:
            raise ValueError


def new_format(hour,minute, am_pm):
    if am_pm=="PM":
        if int(hour)==12:
            new_hour=12
        else:
            new_hour = int(hour) + 12

    else:
        if int(hour)==12:
            new_hour = 0
        else:
            new_hour= int(hour)

    if minute == None:
        new_minute= "00"
    else:
        new_minute=int(minute)

    new_time=f"{new_hour:02}" + ":" + f"{new_minute:02}"

    return new_time





if __name__ == "__main__":
    main()
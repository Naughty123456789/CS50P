import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))



def validate(ip):
    if re.search(r"^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$",ip):
        individual_num=ip.split(".")


        for individual in individual_num:
            if int(individual)<0 or int(individual)>255:
                return False


        return True



    else:
        return False





if __name__ == "__main__":
    main()
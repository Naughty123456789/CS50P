import sys
from pyfiglet import Figlet
import random


def main():
    figlet=Figlet()


    if len(sys.argv)==1:
        user=input("Input:").strip()
        figlet.getFonts()
        print(figlet.renderText(user))

    elif len(sys.argv)==3:
        if sys.argv[1] =="-f" or sys.argv[1] =="--font":

            fonttype=sys.argv[2]
            figlet.getFonts()
            try:

                figlet.setFont(font=fonttype)
                user=input("Input:").strip()
                print(figlet.renderText(user))
            except:
                print("Invalid usage")
                sys.exit(3)






        else:
            print("Invalid usage")
            sys.exit(2)

    else:
        print("Invalid usage")
        sys.exit(1)






main()



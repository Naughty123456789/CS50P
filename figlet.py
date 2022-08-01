import sys
from pyfiglet import Figlet


def main():
    figlet=Figlet()


    if len(sys.argv)==1:
        user=input("Input:").strip()
        figlet.getFonts()
        print(figlet.renderText(user))

    if len(sys.argv)==3:
        if sys.argv[1] =="-f" or sys.argv[1] =="--font":
            user=input("Input:").strip()
            fonttype=sys.argv[2]
            figlet.getFonts()
            figlet.setFont(font=fonttype)
            print(figlet.renderText(user))






        else:
            print("Invalid usage")
            sys.exit(1)






main()



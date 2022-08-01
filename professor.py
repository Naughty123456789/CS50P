import random
import sys


def main():
    level=get_level()
    num_questions=0
    correct_answers=0
    three_tries=1
    while num_questions<10:
        x,y= generate_integer(level)
        answer=input(f"{x}+{y}=")

        if answer.isalpha()==False and (x+y)== int(answer):
            correct_answers+=1

        else:
            print("EEE")
            while True:


                answer=input(f"{x}+{y}=")

                if answer.isalpha()==False and (x+y)==int(answer):
                    correct_answers+=1
                    break



                elif three_tries==2:
                    print(f"{x}+{y}={x+y}")
                    three_tries=1
                    break

                else:
                    print("EEE")
                    three_tries+=1


        num_questions+=1

    print(f"Your score is {correct_answers}")





def get_level():
    while True:
        s=input("Level:").strip()
        if s.isalpha()==False:
            if int(s) ==1 or int(s) ==2 or int(s) ==3:
                return int(s)






def generate_integer(level):
    try:
        if level==1:
            number1=random.randint(0,9)
            number2=random.randint(0,9)
        elif level==2:
            number1=random.randint(10,99)
            number2=random.randint(10,99)
        elif level==3:
            number1=random.randint(100,999)
            number2=random.randint(100,999)

    except ValueError:
        print("ValueError: Level is not 1,2 or 3")
        sys.exit(1)
    return number1,number2






if __name__ == "__main__":
    main()

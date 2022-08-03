import sys


def main():
    raw=input("Fraction:").strip()
    new1=convert(raw)
    last=gauge(new1)
    print(last)


def convert(fraction):
    while True:

        try:

            x,y=fraction.split("/")

            s=int(x)
            z=int(y)
            f=s/z

            if s>z:
                fraction=input("Fraction:")
                continue

            else:
                final=round(f*100)
                if final>100:
                    continue
                else:
                    return final


        except (ValueError,ZeroDivisionError):
            continue




def gauge(percentage):

    if percentage<=1:
        return "E"
    elif 99<=percentage<=100:
        return "F"
    else:
         return str(percentage)+"%"



if __name__ == "__main__":
    main()
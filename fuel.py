def main():
    raw=input("Fraction:").strip()
    new1=convert(raw)
    last=gauge(new1)
    print(last)


def convert(fraction):
    while True:
        try:

            x,y=fraction.split("/")
            if x.isalpha()==True or y.isalpha()==True:
                raise ValueError
            s=int(x)
            z=int(y)

            if s>z:
                raise ValueError
            if z==0:
                raise ZeroDivisionError
        except ValueError:
            return None

        except ZeroDivisionError:
            return None

        final=round((s/z)*100)

        return final





def gauge(percentage):

    if percentage<=1:
        return "E"
    elif 99<=percentage<=100:
        return "F"
    else:
         return f"{percentage}%"



if __name__ == "__main__":
    main()
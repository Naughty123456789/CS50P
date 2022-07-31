def main():
    while True:
        try:
            date=input("Date:").strip()

            if "/" in date:
                x,y,z=date.split("/")
                if x.isalpha():
                    raise UnboundLocalError
                a=int(x)
                b=int(y)
                c=int(z)

                if x.isalpha():
                    raise UnboundLocalError








            elif "," in date:
                x,y,z=date.split(" ")
                if y.isalpha():
                    raise ValueError


                c=int(z)
                b=int(y.replace(",",""))


                mylist=[
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"]
                a=0
                for i in range(len(mylist)):
                    if mylist[i]==x:
                        a=i+1

            if a<1 or a>12:
                raise UnboundLocalError
            if b<1 or b>31:
                raise UnboundLocalError
            print(f'{c}-{a:02}-{b:02}')
            break

        except UnboundLocalError:
            print("Wrong format")
            pass
        except ValueError:
            print("Wrong format")
            pass







main()
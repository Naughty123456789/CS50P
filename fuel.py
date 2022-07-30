def main():


    while True:
        try:
            fraction=input("Fraction:").strip()

            x,y=fraction.split("/")

            s=int(x)
            z=int(y)




            final=round((s/z)*100)

            if final<=1:
                print("E")
                break
            elif 99<=final<=100:
                print("F")
                break
            elif s>z:
                pass
            else:
                print(int(final),"%",sep="")
                break




        except ValueError:
            print("ValueError")
            pass


        except ZeroDivisionError:
            print("Zero Division Error")
            pass




main()
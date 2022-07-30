def main():
    arith=input("Expression:").strip()

    x,y,z=arith.split(" ")

    if y=="+":
        final=float(x)+ float(z)

    elif y=="-":
        final=float(x)-float(z)

    elif y=="*":
        final=float(x)*float(z)

    else:
        final= float(x)/float(z)

    print(final)


main()
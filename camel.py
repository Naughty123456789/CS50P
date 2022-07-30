def main():
    camel=input("camelCase:").strip()
    print("snake_case:",end="")
    checking(camel)
    print("")





def checking(s):

    for i in s:
        if i.isupper():
             print("_"+i.lower(),end="")
        else:
             print(i,end="")



main()

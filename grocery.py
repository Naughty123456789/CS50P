def main():
    d={}
    while True:
        try:
            item=input("").strip().upper()
            if item in d:
                d[item] +=1
            else:
                d[item]=1


        except EOFError:
            print("")
            for i in sorted(d):
                print(d[i],i)
            break






main()
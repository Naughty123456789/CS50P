import inflect



def main():
    p=inflect.engine()
    try:
        mylist=[]
        while True:
            name=input("Name:").strip()


            mylist.append(name)



    except EOFError:
        print("")
        print("Adieu, adieu, to",p.join(mylist))



main()




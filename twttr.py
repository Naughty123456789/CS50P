def main():
    word=input("Input:").strip()

    x=["a","e","i","o","u","A","E","I","O","U"]

    for i in word:
        if i not in x:
            print(i, end="")



    print("")



main()
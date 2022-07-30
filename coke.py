def main():
    required= 50

    while required>0:
        print("Amount due:",required)
        insert_coin=int(input("Insert Coin: "))

        if insert_coin== 25 or insert_coin == 10 or insert_coin==5:
            required-=insert_coin


    if required<=0:
        print("Change owed:",abs(required))



main()


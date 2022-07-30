def main():
    user=input("What time is it ").lower().strip()
    new_formet=convert(user)

    if 7.00 <= new_formet <=8.00:
        print("breakfast time")
    elif 12.00 <= new_formet<=13.00:
        print("lunch time")

    elif 18.00 <= new_formet <=19.00:
        print("dinner time")



def convert(time):
    hour,minute=time.split(":")
    new_minute=float(minute)/60
    new_format=float(hour)+new_minute
    return new_format



if __name__ == "__main__":
    main()
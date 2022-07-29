def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    without_doll=d.replace("$","")
    return float(without_doll)


def percent_to_float(p):
    without_percent=p.replace("%","")
    return float(without_percent/100)



if __name__ == "__main__":
    main()

    

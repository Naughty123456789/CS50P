from datetime import date
import sys
import re
import inflect

p=inflect.engine()

def main():
    user_date = input("What is your birthday:").strip()
    try:
        year,month,day=checking_user_date(user_date)
    except:
        sys.exit("Invalid Date")

    date_user=date(int(year),int(month), int(day))
    date_today=date.today()
    difference= date_today-date_user
    total_minute=difference.days*24*60
    output=p.number_to_words(total_minute, andword="")
    print(output.capitalize(),"minutes")




def checking_user_date(s):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", s):
        year, month,day=s.split("-")
        return year, month,day
from seasons import checking_user_date

def main():
    test_checking_user_date()



def test_checking_user_date():
    assert checking_user_date("1998-07-03")==("1998","07","03")
    assert checking_user_date("cat")==None
    assert checking_user_date("July 3, 1998") ==None


if __name__ == "__main__":
    main()
from numb3rs import validate

def main():
    test_range()
    test_alphabet()
    test_special_case()


def test_range():
    assert validate("255.255.255.255")==True
    assert validate("1.2.3.1000")==False
    assert validate("127.0.0.1")==True
    assert validate("512.512.512.512")==False


def test_alphabet():
    assert validate("cat")==False

def test_special_case():
    assert validate("233....")==False


if __name__ == "__main__":
    main()
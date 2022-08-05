from numb3rs import validate

def main():
    test_range()
    test_alphabet()
    test_format()


def test_range():
    assert validate(r"255.255.255.255")==True
    assert validate(r"1.2.3.1000")==False
    assert validate(r"127.0.0.1")==True
    assert validate(r"512.512.512.512")==False


def test_alphabet():
    assert validate("cat")==False

def test_format():
    assert validate(r"1")==False
    assert validate(r"1.2")==False
    assert validate(r"1.2.3")==False
    assert validate(r"1.2.3.4")== True


if __name__ == "__main__":
    main()
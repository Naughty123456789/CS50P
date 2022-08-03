from plates import is_valid


def main():
    test_at_least_two_letters()
    test_maxsix_mintwo_char()
    test_numbers_to_end_no_middle_no_zero()
    test_no_special_characters()

def test_at_least_two_letters():
    assert is_valid("CS50")== True
    assert is_valid("C500")== False
    assert is_valid("CSR504")==True

def test_maxsix_mintwo_char():
    assert is_valid("CS5675")==True
    assert is_valid("CSR5675")==False
    assert is_valid("CS")==True
    assert is_valid("C")==False

def  test_numbers_to_end_no_middle_no_zero():
    assert is_valid("CS555")==True
    assert is_valid("CS55A")==False
    assert is_valid("CS550")==True
    assert is_valid("CS055")==False


def test_no_special_characters():
    assert is_valid("CS50!")==False
    assert is_valid("!?.,CS50")==False



if __name__ == "__main__":
    main()

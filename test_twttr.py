from twttr import shorten

def main():
    test_vowels_and_caps()
    test_num()
    test_punct()

def test_vowels_and_caps():
    assert shorten("Twitter")=="Twttr"
    assert shorten("Bittergourd")=="Bttrgrd"
    assert shorten("Immediately")=="mmdtly"

def test_num():
    assert shorten("1234")=="1234"

def test_punct():
    assert shorten("?!,.")=="?!,."



if __name__ == "__main__":
    main()
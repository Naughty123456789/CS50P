from twttr import shorten

def main():
    checking_vowels_and_caps()
    checking_num()
    checking_punct()

def checking_vowels_and_caps():
    assert shorten("Twitter")=="Twttr"
    assert shorten("Bittergourd")=="Bttrgrd"
    assert shorten("Immediately")=="mmdtly"

def checking_num():
    assert shorten("1234")=="1234"

def checking_punct():
    assert shorten("?!,.")=="?!,."



if __name__ == "__main__":
    main()
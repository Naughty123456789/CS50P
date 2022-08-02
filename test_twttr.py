from twttr import shorten

def main():
    checking_vowels_and_caps()

def checking_vowels_and_caps():
    assert shorten("Twitter")=="Twttr"
    assert shorten("Bittergourd")=="Bttrgrd"
    assert shorten("Immediately")=="mmdtly"



if __name__ == "__main__":
    main()
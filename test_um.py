from um import count


def main():
    test_special_cases()
    test_normal()
    test_caps()




def test_special_cases():
    assert count("Um, may i um see your album")== 2
    assert count("Big bum")==0
    assert count("UMMM")==1

def test_normal():
    assert count("um")==1
    assert count("um?")==1

def test_caps():
    assert count("Um, thanks")==1
    assert count("Um Um")==2




if __name__ == "__main__":
    main()
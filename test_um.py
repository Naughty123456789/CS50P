from um import count


def main():
    test_special_cases()
    test_normal()
    test_caps()




def test_special_cases():
    assert count("Um, may i see your album")== 1
    assert count("yummy")==0
    assert count("UMMM")==0

def test_normal():
    assert count("Hello um World")==1
    assert count("um?")==1

def test_caps():
    assert count("Um, thanks,um...")==2
    



if __name__ == "__main__":
    main()
from bank import value



def main():
    test_0dollars()
    test_20dollars()
    test_100dollars()



def test_0dollars():
    assert value("hello")=="$0"
    assert value("Hello")=="$0"


def test_20dollars():
    assert value("hi")=="$20"
    assert value("horror")=="$20"

def test_100dollars():
    assert value("I am hungry")=="$100"
    assert value("Pizza")=="$100"











if __name__ == "__main__":
    main()
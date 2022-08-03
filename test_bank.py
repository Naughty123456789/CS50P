from bank import value


def main():
    test_zerodollars()
    test_twentydollars()
    test_hundreddollars()

def test_zerodollars():
    assert value("hello")=="$0"
    assert value("Hello")=="$0"


def test_twentydollars():
    assert value("hi")=="$20"
    assert value("horror")=="$20"
    assert value("heeellloo")=="$20"

def test_hundreddollars():
    assert value("I am hungry")== "$100"
    assert value("Pizza")== "$100"


if __name__ == "__main__":
    main()
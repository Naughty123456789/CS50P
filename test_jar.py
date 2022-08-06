from jar import Jar



def main():
    test_str()
    test_deposit()
    test_withdraw()
    test_init()


def test_init():
    jar=Jar()
    assert jar.capacity ==12
    jar.deposit(3)
    assert jar.capacity ==12





def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar()
    jar.deposit(3)
    assert jar.size==3
    jar.deposit(4)
    assert jar.size==7


def test_withdraw():
    jar=Jar()
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size==7
    jar.withdraw(6)
    assert jar.size==1




if __name__ == "__main__":
    main()
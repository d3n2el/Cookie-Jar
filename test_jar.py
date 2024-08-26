from jar import Jar


def test_init():
    jar= Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar.deposit(5)
    assert jar.size == 5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar= Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_withdraw():
    jar= Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

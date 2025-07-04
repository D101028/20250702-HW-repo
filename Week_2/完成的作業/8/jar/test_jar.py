from jar import Jar

def test_1():
    j = Jar(20)
    assert j.capacity == 20

def test_2():
    j = Jar()
    assert j.size == 0

def test_3():
    j = Jar()
    j.deposit(2)
    assert j.size == 2

def test_4():
    j = Jar()
    j.deposit(12)
    j.withdraw(10)
    assert j.size == 2

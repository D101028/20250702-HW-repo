from numb3rs import validate

def test_1():
    assert validate("0.0.0.0") == True

def test_2():
    assert validate("192.168.1.256") == False

from bank import value

def test_hello_exact():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0
    assert value("Hello, friend") == 0

def test_h_but_not_hello():
    assert value("hi") == 20
    assert value("hey there") == 20
    assert value("Howdy!") == 20

def test_other_greetings():
    assert value("Good morning") == 100
    assert value("What's up") == 100
    assert value("yo") == 100
    assert value("123hello") == 100

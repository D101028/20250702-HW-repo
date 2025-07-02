from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("ABC123") == True
    assert is_valid("XY999") == True

def test_too_short_or_long():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_invalid_start():
    assert is_valid("1CS50") == False
    assert is_valid("C150") == False

def test_number_rules():
    assert is_valid("CS05") == False 
    assert is_valid("CS50X") == False
    assert is_valid("CS0") == False
    assert is_valid("CSX0") == False

def test_non_alnum():
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False
    assert is_valid("CS-50") == False

def test_only_letters():
    assert is_valid("ABCDEF") == True

def test_letters_then_numbers():
    assert is_valid("AB123") == True
    assert is_valid("AB12C") == False

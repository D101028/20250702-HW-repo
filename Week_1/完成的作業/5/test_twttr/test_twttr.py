from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("CS50") == "CS50"

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"

def test_with_punctuation():
    assert shorten("What's up?") == "Wht's p?"

def test_empty_string():
    assert shorten("") == ""

def test_only_vowels():
    assert shorten("aeiouAEIOU") == ""

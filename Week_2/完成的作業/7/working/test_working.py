from working import convert

def test_1():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"

def test_2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_3():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_missing_to_raises():
    try:
        convert("9 AM 5 PM")
    except ValueError:
        assert True
    else:
        assert False, "ValueError not raised when 'to' is missing"

def test_out_of_range_hour():
    for bad in ["13 AM to 5 PM", "0 AM to 5 PM", "9 AM to 13 PM", "9 AM to 0 PM"]:
        try:
            convert(bad)
        except ValueError:
            assert True
        else:
            assert False, f"ValueError not raised for out-of-range hour in '{bad}'"

def test_out_of_range_minute():
    for bad in ["9:60 AM to 5 PM", "9 AM to 5:60 PM", "9:99 AM to 5 PM"]:
        try:
            convert(bad)
        except ValueError:
            assert True
        else:
            assert False, f"ValueError not raised for out-of-range minute in '{bad}'"
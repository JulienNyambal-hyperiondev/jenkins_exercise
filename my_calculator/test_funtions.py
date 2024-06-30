from calc_app import addition

def test_add():
    assert addition(5,5) == 10

def test_add_zero():
    assert addition(0,0) == 0
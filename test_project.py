from project import one, two, three, Three
def test_one():
    assert one() == 5
def test_two():
    assert two() == "Hello World"
def test_three():
    assert isinstance(three(), Three)

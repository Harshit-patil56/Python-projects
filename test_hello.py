from hello import hello


def test_default():
    assert hello("David") == "hello, David"
def test_arg():
     assert hello() == "hello, world"
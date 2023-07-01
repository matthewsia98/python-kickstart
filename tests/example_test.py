def test_example_passing():
    print("This is a passing test")
    assert 1 + 1 == 2


def test_example_failing():
    print("This is a failing test")
    assert 1 + 1 == 3

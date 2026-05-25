from hello import more_hello


def test_hello():
    assert "Hello again!" == more_hello()


def test_hello_again():
    assert "Bye!" == more_hello()

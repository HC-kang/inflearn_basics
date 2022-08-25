def create_token(user_id: str) -> str:
    return user_id + "_verified"


def test_create_token():
    actual = create_token('grab')
    expected = "grab_verified"
    
    assert actual == expected

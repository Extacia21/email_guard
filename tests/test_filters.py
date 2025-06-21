from email_guard.filters import is_blacklisted


def test_blacklist():
    assert is_blacklisted("user@fraud.net")
    assert not is_blacklisted("person@legit.com")

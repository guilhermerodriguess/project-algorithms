from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError) as err:
        encrypt_message("message", "invalid_key")
    assert str(err.value) == "tipo inválido para key"

    with pytest.raises(TypeError) as err:
        encrypt_message(123, 2)
    assert str(err.value) == "tipo inválido para message"

    encrypted = encrypt_message("message", 10)
    assert encrypted == "egassem", f"Expected 'egassem', got '{encrypted}'"

    encrypted = encrypt_message("message", 3)
    assert encrypted == "sem_egas", f"Expected 'sem_egas', got '{encrypted}'"

    encrypted = encrypt_message("message", 4)
    assert encrypted == "ega_ssem", f"Expected 'ega_ssem', got '{encrypted}'"

    encrypted = encrypt_message("message", 0)
    assert encrypted == "egassem", f"Expected 'egassem', got '{encrypted}'"

    encrypted = encrypt_message("message", 1)
    assert encrypted == "m_egasse", f"Expected 'm_egasse', got '{encrypted}'"

    encrypted = encrypt_message("", 2)
    assert encrypted == "", f"Expected '', got '{encrypted}'"

    encrypted = encrypt_message("", 0)
    assert encrypted == "", f"Expected '', got '{encrypted}'"

    encrypted = encrypt_message("a", 1)
    assert encrypted == "a", f"Expected 'a', got '{encrypted}'"

    print("All tests passed!")


test_encrypt_message()

import pytest
from reverser import reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    assert reverse_string("12345") == "54321"

if __name__ == "__main__":
    pytest.main()
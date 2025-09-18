from homework1.src.task6 import words_in_file
import pytest

@pytest.mark.parametrize(
    "filename, expected_count",
    [
        ("task6_read_me.txt", 127),
    ]
)

def test_words_in_file(filename, expected_count):
    """
    Parameterized test for the words_in_file function.
    Verifies that the word count matches the expected count.
    """
    assert words_in_file(filename) == expected_count

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        words_in_file("not_a_file.txt")
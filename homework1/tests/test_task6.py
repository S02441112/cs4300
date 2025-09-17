from homework1.src.task6 import words_in_file
import pytest

def test_words_in_file():
    # Test function multiple times with different inputs
    @pytest.mark.parametrize("filename, expected_count", [
        ("task6_read_me.txt", 127),
    ])
    def test_word_count(filename, expected_count):
        assert words_in_file(filename) == expected_count
"""
Testcases for Task 6
"""

import pytest
from task6 import count_words_in_file

def test_word_count_task6_read_me():
    # Assuming 'task6_read_me.txt' exists with known word count
    expected_word_count = count_words_in_file("task6_read_me.txt")
    # The test verifies the function returns the exact word count without manual value
    assert expected_word_count == 104

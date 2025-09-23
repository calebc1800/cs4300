"""
Task 5: Lists and Dictionaries
"""

import pytest
from task5 import (create_favorite_books, print_first_three_books, create_student_dict)

class TestFavoriteBooks:
    """
    Test cases for favorite books list operations.
    """

    def test_create_favorite_books_structure(self):
        """
        Test that create_favorite_books returns correct structure.
        """
        books = create_favorite_books()

        # Check it's a list
        assert isinstance(books, list)

        # Check it has content
        assert len(books) > 0

        # Check each book has correct structure
        for book in books:
            assert isinstance(book, dict)
            assert 'title' in book
            assert 'author' in book
            assert isinstance(book['title'], str)
            assert isinstance(book['author'], str)

    def test_create_favorite_books_content(self):
        """
        Test specific content of favorite books.
        """
        books = create_favorite_books()

        # Check for specific books
        titles = [book['title'] for book in books]
        assert "The Way of Kings" in titles
        assert "Ender's Game" in titles
        assert "Skyward" in titles

    def test_print_first_three_books(self):
        """
        Test list slicing functionality.
        """
        books = create_favorite_books()
        first_three = print_first_three_books(books)

        # Check return value
        assert isinstance(first_three, list)
        assert len(first_three) == 3

        # Check it matches the first three from original list
        assert first_three == books[:3]

class TestStudentdictionary:
    """
    Test cases for student dictionary.
    """

    def test_create_student_dict_structure(self):
        """
        Test that create_student_dictionary returns correct structure.
        """
        db = create_student_dict()

        # Check it's a dictionary
        assert isinstance(db, dict)

        # Check it has content
        assert len(db) > 0

        # Check structure - names as keys, IDs as values
        for name, student_id in db.items():
            assert isinstance(name, str)
            assert isinstance(student_id, str)
            assert student_id.startswith("ST")

    def test_create_student_dict_content(self):
        """
        Test specific content of student dictionary.
        """
        db = create_student_dict()

        # Check for specific students
        assert "Alice Johnson" in db
        assert "Bob Smith" in db
        assert "Carol Davis" in db

        # Check ID format
        for student_id in db.values():
            assert len(student_id) == 5  # ST + 3 digits
            assert student_id[:2] == "ST"
            assert student_id[2:].isdigit()

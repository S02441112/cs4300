from src.task5 import first_three_books, student_id

def test_first_three_books_length():
    """
    Verify first_three_books() returns exactly 3 books.
    Ensures correct use of list slicing.
    """
    books = first_three_books()
    assert len(books) == 3, "Should return exactly 3 books"

def test_first_three_books_content():
    """
    Verify that returned books are structured properly.
    Each book should be a tuple (title, author), both strings.
    """
    books = first_three_books()
    for book in books:
        assert isinstance(book, tuple)
        assert len(book) == 2
        assert all(isinstance(field, str) for field in book)

def test_first_three_books_slice_correctness():
    """
    Verify first three books are sliced correctly
    and match the expected hardcoded list.
    """
    assert first_three_books() == [
        ("Dune", "Frank Herbert"),
        ("Neuromancer", "William Gibson"),
        ("Snow Crash", "Neal Stephenson")
    ]

def test_student_id_key_value_types():
    """
    Verify student_id() function returns dictionary
    with string keys (names) and string values (student IDs).
    """
    students = student_id()
    for name, sid in students.items():
        assert isinstance(name, str)
        assert isinstance(sid, str)

def test_student_lookup():
    """
    Verify specific students can be looked up by name
    and their student IDs match expected values.
    """
    students = student_id()
    assert students["Alice"] == "S1234"
    assert students["Bob"] == "S5678"
    assert students["Charlie"] == "S9101"

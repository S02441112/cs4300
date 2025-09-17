from homework1.src.task5 import first_three_books, student_id

def test_first_three_books_length():
    books = first_three_books()
    assert len(books) == 3, "Should return exactly 3 books"

def test_first_three_books_content():
    books = first_three_books()
    # Ensure each book is a (title, author) tuple
    for book in books:
        assert isinstance(book, tuple)
        assert len(book) == 2
        assert all(isinstance(field, str) for field in book)

def test_first_three_books_slice_correctness():
    assert first_three_books() == [
        ("Dune", "Frank Herbert"),
        ("Neuromancer", "William Gibson"),
        ("Snow Crash", "Neal Stephenson")
    ]

def test_student_id_key_value_types():
    students = student_id()
    for name, sid in students.items():
        assert isinstance(name, str)
        assert isinstance(sid, str)

def test_student_lookup():
    students = student_id()
    assert students["Alice"] == "S1234"
    assert students["Bob"] == "S5678"
    assert students["Charlie"] == "S9101"

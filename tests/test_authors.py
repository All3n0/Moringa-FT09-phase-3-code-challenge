from models.author import Author

def test_author_class():
    # Test 1: Create an author and check its attributes
    try:
        author = Author(1, "John Doe")
        assert author.id == 1
        assert author.name == "John Doe"
        print(f"Test 1 Passed: {author}")
    except Exception as e:
        print(f"Test 1 Failed: {e}")

    # Test 2: Attempt to change the name (should raise an exception)
    try:
        author.name = "Jane Doe"
    except AttributeError as e:
        print(f"Test 2 Passed: {e}")
    except Exception as e:
        print(f"Test 2 Failed: Unexpected exception {e}")

    # Test 3: Attempt to create an author with a non-integer ID (should raise an exception)
    try:
        author_invalid_id = Author("one", "John Doe")
    except TypeError as e:
        print(f"Test 3 Passed: {e}")
    except Exception as e:
        print(f"Test 3 Failed: Unexpected exception {e}")

    # Test 4: Attempt to create an author with an empty name (should raise an exception)
    try:
        author_invalid_name = Author(2, "")
    except ValueError as e:
        print(f"Test 4 Passed: {e}")
    except Exception as e:
        print(f"Test 4 Failed: Unexpected exception {e}")

if __name__ == "__main__":
    test_author_class()

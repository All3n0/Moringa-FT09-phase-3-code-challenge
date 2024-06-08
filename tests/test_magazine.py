from models.magazine import Magazine

def test_magazine_class():
    # Test 1: Create a magazine and check its attributes
    try:
        magazine = Magazine(1, "Tech Today", "Technology")
        assert magazine.id == 1
        assert magazine.name == "Tech Today"
        assert magazine.category == "Technology"
        print(f"Test 1 Passed: {magazine}")
    except Exception as e:
        print(f"Test 1 Failed: {e}")

    # Test 2: Attempt to change the name within valid constraints
    try:
        magazine.name = "Health Weekly"
        assert magazine.name == "Health Weekly"
        print(f"Test 2 Passed: {magazine}")
    except Exception as e:
        print(f"Test 2 Failed: {e}")

    # Test 3: Attempt to change the category within valid constraints
    try:
        magazine.category = "Health"
        assert magazine.category == "Health"
        print(f"Test 3 Passed: {magazine}")
    except Exception as e:
        print(f"Test 3 Failed: {e}")

    # Test 4: Attempt to set an invalid id (should raise an exception)
    try:
        magazine.id = "one"
    except TypeError as e:
        print(f"Test 4 Passed: {e}")
    except Exception as e:
        print(f"Test 4 Failed: Unexpected exception {e}")

    # Test 5: Attempt to set an invalid name (should raise an exception)
    try:
        magazine.name = "T"  # Name too short
    except ValueError as e:
        print(f"Test 5 Passed: {e}")
    except Exception as e:
        print(f"Test 5 Failed: Unexpected exception {e}")

    # Test 6: Attempt to set an invalid category (should raise an exception)
    try:
        magazine.category = ""  # Category too short
    except TypeError as e:
        print(f"Test 6 Passed: {e}")
    except Exception as e:
        print(f"Test 6 Failed: Unexpected exception {e}")

if __name__ == "__main__":
    test_magazine_class()

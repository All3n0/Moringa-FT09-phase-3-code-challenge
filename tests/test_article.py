from models.article import Article
from models.author import Author
from models.magazine import Magazine

def test_article_class():
    # Mock objects for Author and Magazine
    class MockAuthor:
        def __init__(self, id, name):
            self.id = id
            self.name = name

    class MockMagazine:
        def __init__(self, id, name, category):
            self.id = id
            self.name = name
            self.category = category

    # Create mock author and magazine instances
    author = MockAuthor(1, "John Doe")
    magazine = MockMagazine(1, "Tech Today", "Technology")

    # Test 1: Create an article and check its attributes
    try:
        article = Article(author, magazine, "Understanding AI")
        assert article.title == "Understanding AI"
        assert article.author.id == 1
        assert article.magazine.id == 1
        print(f"Test 1 Passed: {article}")
    except Exception as e:
        print(f"Test 1 Failed: {e}")

    # Test 2: Attempt to change the title (should raise an exception)
    try:
        article.title = "AI in Depth"
    except AttributeError as e:
        print(f"Test 2 Passed: {e}")
    except Exception as e:
        print(f"Test 2 Failed: Unexpected exception {e}")

    # Test 3: Attempt to create an article with a title that is too short
    try:
        article_short_title = Article(author, magazine, "AI")
    except ValueError as e:
        print(f"Test 3 Passed: {e}")
    except Exception as e:
        print(f"Test 3 Failed: Unexpected exception {e}")

    # Test 4: Attempt to create an article with a title that is too long
    try:
        article_long_title = Article(author, magazine, "A" * 51)
    except ValueError as e:
        print(f"Test 4 Passed: {e}")
    except Exception as e:
        print(f"Test 4 Failed: Unexpected exception {e}")

if __name__ == "__main__":
    test_article_class()

from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database
    create_tables()

    # Get user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Clear the database
    # cursor.execute('DELETE FROM authors')
    # cursor.execute('DELETE FROM magazines')
    # cursor.execute('DELETE FROM articles')
    
    # cursor.execute('''
    #     DELETE FROM authors 
    #     WHERE id NOT IN (SELECT id FROM authors ORDER BY id DESC LIMIT 5)
    # ''')
    # cursor.execute('''
    #     DELETE FROM magazines 
    #     WHERE id NOT IN (SELECT id FROM magazines ORDER BY id DESC LIMIT 5)
    # ''')
    # cursor.execute('''
    #     DELETE FROM articles 
    #     WHERE id NOT IN (SELECT id FROM articles ORDER BY id DESC LIMIT 5)
    # ''')
    # conn.commit()
    # Check if the author already exists
    cursor.execute('SELECT id FROM authors WHERE name = ?', (author_name,))
    author_info = cursor.fetchone()

    if author_info:
        author_id = author_info[0]
    else:
        # Insert the new author
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
        author_id = cursor.lastrowid

    # Check if the magazine already exists
    cursor.execute('SELECT id FROM magazines WHERE name = ?', (magazine_name,))
    magazine_info = cursor.fetchone()

    if magazine_info:
        magazine_id = magazine_info[0]
    else:
        # Insert the new magazine
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
        magazine_id = cursor.lastrowid

    conn.commit()
    conn.close()

    # Create the Article instance
    article = Article(None, article_title, article_content, author_id, magazine_id)

    # Display the updated database content
    display_all()

def display_all():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch authors
    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    # Fetch articles
    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    # Fetch magazines
    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    # Close connection
    conn.close()

    # Display authors
    print("\nAuthors:")
    for author in authors:
        print(Author(author["id"], author["name"]))

    # Display articles
    print("\nArticles:")
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

    # Display magazines
    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))
     # Delete excess entries
    
    conn.close()
     #DELETING TO REMAIN WITH ONLY FIVE OF EACH
   
    # cursor.execute('DELETE FROM magazines WHERE id NOT IN (SELECT id FROM magazines ORDER BY id LIMIT 5)')
    # cursor.execute('DELETE FROM authors WHERE id NOT IN (SELECT id FROM authors ORDER BY id LIMIT 5)')
    # cursor.execute('DELETE FROM articles WHERE id NOT IN (SELECT id FROM articles ORDER BY id LIMIT 5)')

    # conn.commit()
if __name__ == "__main__":
    main()

import mysql.connector
from mysql.connector import Error

# Function to connect to MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',      # Replace with your MySQL server hostname or IP
            user='root',           # Replace with your MySQL username
            password='123456',     # Replace with your MySQL password
            database='library_db'  # Replace with your database name
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        else:
            print("Connection failed.")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# Function to fetch and print all books
def fetch_all_books():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            if books:
                print("\nBooks in the library:")
                for book in books:
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Genre: {book[4]}")
            else:
                print("No books found.")
        except mysql.connector.Error as e:
            print(f"Error fetching books: {e}")
        finally:
            cursor.close()
            connection.close()
            print("MySQL connection closed")

# Function to add a new book
def add_book(title, author, published_year, genre):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            query = "INSERT INTO books (title, author, published_year, genre) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (title, author, published_year, genre))
            connection.commit()
            print("Book added successfully.")
        except mysql.connector.Error as e:
            print(f"Error adding book: {e}")
        finally:
            cursor.close()
            connection.close()
            print("MySQL connection closed")

# Function to update a book by book_id
def update_book(book_id, title, author, published_year, genre):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            query = "UPDATE books SET title = %s, author = %s, published_year = %s, genre = %s WHERE book_id = %s"
            cursor.execute(query, (title, author, published_year, genre, book_id))
            connection.commit()
            print("Book updated successfully.")
        except mysql.connector.Error as e:
            print(f"Error updating book: {e}")
        finally:
            cursor.close()
            connection.close()
            print("MySQL connection closed")

# Function to delete a book by book_id
def delete_book(book_id):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            query = "DELETE FROM books WHERE book_id = %s"
            cursor.execute(query, (book_id,))
            connection.commit()
            print("Book deleted successfully.")
        except mysql.connector.Error as e:
            print(f"Error deleting book: {e}")
        finally:
            cursor.close()
            connection.close()
            print("MySQL connection closed")

# Main function to handle user input and menu options
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            published_year = input("Enter published year: ")
            genre = input("Enter genre: ")
            add_book(title, author, published_year, genre)
            
        elif choice == '2':
            fetch_all_books()
                
        elif choice == '3':
            book_id = input("Enter book ID to update: ")
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            published_year = input("Enter new published year: ")
            genre = input("Enter new genre: ")
            update_book(book_id, title, author, published_year, genre)

        elif choice == '4':
            book_id = input("Enter book ID to delete: ")
            delete_book(book_id)
        
        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

"""
Task 5: Lists and Directories
"""

def create_favorite_books():
    """
    Create a list of my favorite books with titles and their authors.

    Returns:
        list: List of dictionaries containing book information
    """
    books = [
        {"title": "The Way of Kings", "author": "Brandon Sanderson"}, 
        {"title": "Legend", "author": "Marie Lu"},
        {"title": "Ender's Game", "author": "Orson Scott Card"},
        {"title": "Words of Radiance", "author": "Brandon Sanderson"}, 
        {"title": "Mistborn: The Final Empire", "author": "Brandon Sanderson"}, 
        {"title": "Skyward", "author": "Brandon Sanderson"}, 
        {"title": "Tress of the Emerald Sea", "author": "Brandon Sanderson"}, 
        {"title": "Steelheart", "author": "Brandon Sanderson"}
    ]

    return books

def print_first_three_books(books):
    """
    Uses list slicing to print the first three books in the list.

    Args:
        books (list): List of book dictionaries

    Returns:
        list: First three books
    """
    first_three = books[:3]

    print("First three books:")
    for i, book in enumerate(first_three, 1):
        print(f"{i}. '{book['title']}' by {book['author']}")

    return first_three

def create_student_dict():
    """
    Create a dictionary of student names and ids.

    Returns:
        dict: Student database with names as keys and IDs as values
    """
    student_dict = {
        "Alice Johnson": "ST001",
        "Bob Smith": "ST002", 
        "Carol Davis": "ST003",
        "David Wilson": "ST004",
        "Emma Brown": "ST005",
        "Frank Miller": "ST006",
        "Grace Lee": "ST007"
    }

    return student_dict

def display_student_dict(student_dict):
    """
    Display the student dictionary in a formatted way.

    Args:
        student_db (dict): Student dictionary
    """
    print("\nStudent Dictionary:")
    print("-" * 30)
    for name, student_id in student_dict.items():
        print(f"{student_id}: {name}")

if __name__ == "__main__":
    # Demonstrate lists and list slicing
    books = create_favorite_books()
    first_three = print_first_three_books(books)

    # Demonstrate dictionaries
    students = create_student_dict()
    display_student_dict(students)

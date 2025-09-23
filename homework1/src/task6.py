"""
Task 6: File Handling and Metaprogramming
"""

import os

def count_words_in_file(filename):
    """
    Reads a file and counts the number of words.
    """
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words)

if __name__ == "__main__":
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct path to task6_read_me.txt file
    file_path = os.path.join(script_dir, '..', 'task6_read_me.txt')
    # Normalize the path
    file_path = os.path.normpath(file_path)
    
    word_count = count_words_in_file(file_path)
    print(f"Number of words in {file_path}: {word_count}")

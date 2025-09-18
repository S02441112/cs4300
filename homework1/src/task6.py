import os

def words_in_file(filename):
    """
    Reads a text file and counts the number of words.
    Args:
        filename (str): Path to the file to be read.
    Returns:
        int: Word count in the file.
    """
    # Make path relative to homework1/ (where the txt file is stored)
    base_dir = os.path.dirname(os.path.dirname(__file__))  # go up one dir from src/
    file_path = os.path.join(base_dir, filename)

    with open(file_path, "r") as f:
        return len(f.read().split())

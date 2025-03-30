"""
Module: thats_the_way
Lists files in a directory that start with 'deep'.
"""
import os

def thats_the_way(path_to_directory):
    """
    Returns a list of files in the given directory that start with 'deep'.
    :param path_to_directory: Path to the directory
    :return: List of matching file names
    """
    try:
        return [file for file in os.listdir(path_to_directory) if file.startswith("deep")]
    except FileNotFoundError:
        print(f"Error: The directory '{path_to_directory}' does not exist.")
        return []

if __name__ == "__main__":
    # Check the images folder
    matching_files = thats_the_way(os.getcwd())
    print(matching_files)
    

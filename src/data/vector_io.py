"""
Vector save and load operations.
"""
import numpy as np
from src.utils.validators import validate_file_exists, validate_directory_exists
import os


def save_vectors(vectors, categories, file_path):
    """
    Save vectors to text file with category labels.

    Args:
        vectors: NumPy array of vectors
        categories: List of category labels
        file_path: Output file path
    """
    validate_directory_exists(os.path.dirname(file_path))

    with open(file_path, "w") as f:
        for category, vector in zip(categories, vectors):
            vector_str = ", ".join(f"{v:.6f}" for v in vector)
            f.write(f"{category}: [{vector_str}]\n")


def load_vectors(file_path):
    """
    Load vectors from text file.

    Args:
        file_path: Input file path

    Returns:
        tuple: (vectors as NumPy array, categories as list)

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    validate_file_exists(file_path)

    vectors = []
    categories = []

    with open(file_path, "r") as f:
        for line in f:
            if not line.strip():
                continue

            category, vector_str = line.split(": [", 1)
            vector_str = vector_str.rstrip("]\n")
            vector = [float(x) for x in vector_str.split(", ")]

            categories.append(category)
            vectors.append(vector)

    return np.array(vectors), categories

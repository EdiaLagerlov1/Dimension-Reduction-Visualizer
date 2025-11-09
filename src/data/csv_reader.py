"""
CSV file reading utilities.
"""
import pandas as pd
from src.utils.validators import validate_file_exists


def read_csv_data(file_path):
    """
    Read sentences and categories from CSV file.

    Args:
        file_path: Path to CSV file

    Returns:
        tuple: (sentences, categories) as lists

    Raises:
        FileNotFoundError: If CSV file doesn't exist
        ValueError: If CSV format is invalid
    """
    validate_file_exists(file_path)

    df = pd.read_csv(file_path)

    if "category" not in df.columns or "sentence" not in df.columns:
        raise ValueError("CSV must have 'category' and 'sentence' columns")

    sentences = df["sentence"].tolist()
    categories = df["category"].tolist()

    return sentences, categories


def get_unique_categories(categories):
    """
    Get unique categories from list.

    Args:
        categories: List of category labels

    Returns:
        list: Unique categories sorted
    """
    return sorted(list(set(categories)))

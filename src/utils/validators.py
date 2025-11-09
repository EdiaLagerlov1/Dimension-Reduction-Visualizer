"""
Input validation utilities.
"""
import os


def validate_file_exists(file_path):
    """
    Validate that a file exists.

    Args:
        file_path: Path to the file

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")


def validate_directory_exists(dir_path):
    """
    Validate that a directory exists, create if it doesn't.

    Args:
        dir_path: Path to the directory
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def validate_data_shape(data, expected_dim=None):
    """
    Validate data shape for dimension reduction.

    Args:
        data: NumPy array
        expected_dim: Expected number of dimensions

    Raises:
        ValueError: If data shape is invalid
    """
    if len(data) == 0:
        raise ValueError("Data is empty")

    if expected_dim and data.shape[1] < expected_dim:
        raise ValueError(
            f"Data has {data.shape[1]} features, need at least {expected_dim}"
        )

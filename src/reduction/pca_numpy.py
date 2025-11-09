"""
PCA implementation using NumPy.
"""
import numpy as np
from src.utils import config
from src.utils.validators import validate_data_shape


def compute_pca_numpy(data, n_components=config.N_COMPONENTS):
    """
    Compute PCA using NumPy.

    Args:
        data: NumPy array of shape (n_samples, n_features)
        n_components: Number of components to keep

    Returns:
        NumPy array: Transformed data (n_samples, n_components)

    Raises:
        ValueError: If data shape is invalid
    """
    validate_data_shape(data, n_components)

    # Center the data
    mean = np.mean(data, axis=0)
    centered_data = data - mean

    # Compute covariance matrix
    cov_matrix = np.cov(centered_data.T)

    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # Sort by eigenvalues (descending)
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Select top n_components
    components = eigenvectors[:, :n_components]

    # Transform data
    transformed = centered_data @ components

    return transformed.real


def run_pca_numpy(vectors, categories):
    """
    Run PCA using NumPy and return 3D result.

    Args:
        vectors: NumPy array of vectors
        categories: List of category labels

    Returns:
        NumPy array: 3D PCA result
    """
    return compute_pca_numpy(vectors, n_components=config.N_COMPONENTS)

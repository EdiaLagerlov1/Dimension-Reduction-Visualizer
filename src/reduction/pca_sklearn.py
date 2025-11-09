"""
PCA implementation using scikit-learn.
"""
from sklearn.decomposition import PCA
from src.utils import config
from src.utils.validators import validate_data_shape


def compute_pca_sklearn(data, n_components=config.N_COMPONENTS):
    """
    Compute PCA using scikit-learn.

    Args:
        data: NumPy array of shape (n_samples, n_features)
        n_components: Number of components to keep

    Returns:
        NumPy array: Transformed data (n_samples, n_components)

    Raises:
        ValueError: If data shape is invalid
    """
    validate_data_shape(data, n_components)

    pca = PCA(n_components=n_components)
    transformed = pca.fit_transform(data)

    return transformed


def run_pca_sklearn(vectors, categories):
    """
    Run PCA using scikit-learn and return 3D result.

    Args:
        vectors: NumPy array of vectors
        categories: List of category labels

    Returns:
        NumPy array: 3D PCA result
    """
    return compute_pca_sklearn(vectors, n_components=config.N_COMPONENTS)

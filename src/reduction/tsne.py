"""
t-SNE implementation using scikit-learn.
"""
from sklearn.manifold import TSNE
from src.utils import config
from src.utils.validators import validate_data_shape


def compute_tsne(data, n_components=config.N_COMPONENTS):
    """
    Compute t-SNE using scikit-learn.

    Args:
        data: NumPy array of shape (n_samples, n_features)
        n_components: Number of components to keep

    Returns:
        NumPy array: Transformed data (n_samples, n_components)

    Raises:
        ValueError: If data shape is invalid
    """
    validate_data_shape(data, n_components)

    tsne = TSNE(
        n_components=n_components,
        perplexity=config.TSNE_PERPLEXITY,
        max_iter=config.TSNE_ITERATIONS,
        random_state=42
    )
    transformed = tsne.fit_transform(data)

    return transformed


def run_tsne(vectors, categories):
    """
    Run t-SNE and return 3D result.

    Args:
        vectors: NumPy array of vectors
        categories: List of category labels

    Returns:
        NumPy array: 3D t-SNE result
    """
    return compute_tsne(vectors, n_components=config.N_COMPONENTS)

"""
Alignment utilities for PCA results.
"""
import numpy as np


def align_pca_signs(reference, target):
    """
    Align signs of PCA components to match reference.

    Args:
        reference: Reference PCA result (n_samples, n_components)
        target: Target PCA result to align (n_samples, n_components)

    Returns:
        NumPy array: Aligned target with flipped signs where needed
    """
    aligned = target.copy()

    for i in range(target.shape[1]):
        # Compute correlation between components
        correlation = np.corrcoef(reference[:, i], target[:, i])[0, 1]

        # If negative correlation, flip the sign
        if correlation < 0:
            aligned[:, i] = -aligned[:, i]

    return aligned

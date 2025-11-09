"""
3D visualization utilities.
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from src.utils import config
from src.utils.validators import validate_directory_exists
from src.utils.colors import get_category_colors
import os


def plot_3d_scatter(data, categories, title, output_path):
    """
    Create and save 3D scatter plot.

    Args:
        data: NumPy array of 3D coordinates (n_samples, 3)
        categories: List of category labels
        title: Plot title
        output_path: Path to save the plot

    Raises:
        ValueError: If data is not 3D
    """
    if data.shape[1] != 3:
        raise ValueError(f"Expected 3D data, got {data.shape[1]} dimensions")

    validate_directory_exists(os.path.dirname(output_path))

    # Create figure
    fig = plt.figure(figsize=config.FIGURE_SIZE)
    ax = fig.add_subplot(111, projection='3d')

    # Get unique categories and color mapping
    unique_categories = sorted(list(set(categories)))
    category_colors = get_category_colors(categories)

    # Plot each category with consistent colors
    for category in unique_categories:
        mask = [cat == category for cat in categories]
        category_data = data[mask]

        ax.scatter(
            category_data[:, 0],
            category_data[:, 1],
            category_data[:, 2],
            c=category_colors[category],
            label=category,
            s=config.POINT_SIZE,
            alpha=config.ALPHA,
            edgecolors='black',
            linewidth=0.5
        )

    ax.set_xlabel('Component 1')
    ax.set_ylabel('Component 2')
    ax.set_zlabel('Component 3')
    ax.set_title(title)
    ax.legend()

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Visualization saved to: {output_path}")

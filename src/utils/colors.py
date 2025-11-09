"""
Color mapping utilities for visualization.
"""
from src.utils import config


def get_category_colors(categories):
    """
    Create consistent color mapping for categories.

    Args:
        categories: List of category labels

    Returns:
        dict: Mapping from category to color hex code
    """
    unique_categories = sorted(list(set(categories)))
    color_map = {}

    for i, category in enumerate(unique_categories):
        # Use color from palette, cycle if more categories than colors
        color_index = i % len(config.COLOR_PALETTE)
        color_map[category] = config.COLOR_PALETTE[color_index]

    return color_map

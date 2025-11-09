"""
t-SNE workflow.
"""
from src.data.vector_io import load_vectors
from src.reduction.tsne import run_tsne
from src.visualization.plotter import plot_3d_scatter
from src.utils import config
from src.utils.timing import Timer, save_runtime


def run_tsne_visualization():
    """Run t-SNE and visualize."""
    print("=" * 50)
    print("RUNNING t-SNE")
    print("=" * 50)

    # Load vectors
    print(f"Loading vectors from: {config.OUTPUT_VECTORS_PATH}")
    vectors, categories = load_vectors(config.OUTPUT_VECTORS_PATH)
    print(f"Loaded {len(vectors)} vectors")

    # t-SNE
    print("\nRunning t-SNE...")
    with Timer() as tsne_timer:
        tsne_result = run_tsne(vectors, categories)
    save_runtime(tsne_timer.elapsed(), "t-SNE", config.OUTPUT_RUNTIME_PATH)

    plot_3d_scatter(
        tsne_result,
        categories,
        "t-SNE Visualization",
        config.OUTPUT_TSNE_PATH
    )

    print("t-SNE complete!\n")

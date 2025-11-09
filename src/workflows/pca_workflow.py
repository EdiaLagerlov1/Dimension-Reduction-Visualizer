"""
PCA workflow.
"""
from src.data.vector_io import load_vectors, save_vectors
from src.reduction.pca_numpy import run_pca_numpy
from src.reduction.pca_sklearn import run_pca_sklearn
from src.visualization.plotter import plot_3d_scatter
from src.utils import config
from src.utils.alignment import align_pca_signs
from src.utils.timing import Timer, save_runtime


def run_pca():
    """Run both PCA implementations and visualize."""
    print("=" * 50)
    print("RUNNING PCA")
    print("=" * 50)

    # Load vectors
    print(f"Loading vectors from: {config.OUTPUT_VECTORS_PATH}")
    vectors, categories = load_vectors(config.OUTPUT_VECTORS_PATH)
    print(f"Loaded {len(vectors)} vectors")

    # NumPy PCA
    print("\nRunning PCA with NumPy...")
    with Timer() as numpy_timer:
        pca_numpy_result = run_pca_numpy(vectors, categories)
    save_runtime(numpy_timer.elapsed(), "PCA (NumPy)", config.OUTPUT_RUNTIME_PATH)
    save_vectors(pca_numpy_result, categories, config.OUTPUT_PCA_NUMPY_VECTORS_PATH)
    print(f"NumPy PCA vectors saved to: {config.OUTPUT_PCA_NUMPY_VECTORS_PATH}")
    plot_3d_scatter(
        pca_numpy_result,
        categories,
        "PCA (NumPy Implementation)",
        config.OUTPUT_PCA_NUMPY_PATH
    )

    # Sklearn PCA
    print("\nRunning PCA with scikit-learn...")
    with Timer() as sklearn_timer:
        pca_sklearn_result = run_pca_sklearn(vectors, categories)
    save_runtime(sklearn_timer.elapsed(), "PCA (Scikit-learn)", config.OUTPUT_RUNTIME_PATH)

    # Align sklearn result to numpy result
    print("Aligning sklearn PCA components to match numpy PCA...")
    pca_sklearn_result = align_pca_signs(pca_numpy_result, pca_sklearn_result)

    save_vectors(pca_sklearn_result, categories, config.OUTPUT_PCA_SKLEARN_VECTORS_PATH)
    print(f"Sklearn PCA vectors saved to: {config.OUTPUT_PCA_SKLEARN_VECTORS_PATH}")
    plot_3d_scatter(
        pca_sklearn_result,
        categories,
        "PCA (Scikit-learn Implementation) - Aligned",
        config.OUTPUT_PCA_SKLEARN_PATH
    )

    print("PCA complete!\n")

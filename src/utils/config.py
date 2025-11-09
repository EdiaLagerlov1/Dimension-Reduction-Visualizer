"""
Configuration constants for the Dimension Reduction Visualizer.
"""
import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# File names
INPUT_CSV = "sentences.csv"
OUTPUT_VECTORS = "vectors.txt"
OUTPUT_PCA_NUMPY = "PCA_numpy.png"
OUTPUT_PCA_SKLEARN = "PCA_sklearn.png"
OUTPUT_TSNE = "Tsne.png"
OUTPUT_PCA_NUMPY_VECTORS = "PCA_numpy_vectors.txt"
OUTPUT_PCA_SKLEARN_VECTORS = "PCA_sklearn_vectors.txt"
OUTPUT_RUNTIME = "runtime.txt"

# Full paths
INPUT_CSV_PATH = os.path.join(INPUT_DIR, INPUT_CSV)
OUTPUT_VECTORS_PATH = os.path.join(OUTPUT_DIR, OUTPUT_VECTORS)
OUTPUT_PCA_NUMPY_PATH = os.path.join(OUTPUT_DIR, OUTPUT_PCA_NUMPY)
OUTPUT_PCA_SKLEARN_PATH = os.path.join(OUTPUT_DIR, OUTPUT_PCA_SKLEARN)
OUTPUT_TSNE_PATH = os.path.join(OUTPUT_DIR, OUTPUT_TSNE)
OUTPUT_PCA_NUMPY_VECTORS_PATH = os.path.join(OUTPUT_DIR, OUTPUT_PCA_NUMPY_VECTORS)
OUTPUT_PCA_SKLEARN_VECTORS_PATH = os.path.join(OUTPUT_DIR, OUTPUT_PCA_SKLEARN_VECTORS)
OUTPUT_RUNTIME_PATH = os.path.join(OUTPUT_DIR, OUTPUT_RUNTIME)

# Word2Vec parameters
WORD2VEC_VECTOR_SIZE = 100
WORD2VEC_WINDOW = 5
WORD2VEC_MIN_COUNT = 1
WORD2VEC_WORKERS = 4
WORD2VEC_EPOCHS = 100

# Dimension reduction parameters
N_COMPONENTS = 3
TSNE_PERPLEXITY = 10
TSNE_ITERATIONS = 1000

# Visualization parameters
FIGURE_SIZE = (10, 8)
POINT_SIZE = 50
ALPHA = 0.7

# Color palette for categories (consistent across all visualizations)
COLOR_PALETTE = [
    "#FF6B6B",  # Red
    "#4ECDC4",  # Teal
    "#FFE66D",  # Yellow
    "#95E1D3",  # Mint
    "#F38181",  # Pink
    "#AA96DA",  # Purple
    "#FCBAD3",  # Light Pink
    "#A8D8EA",  # Sky Blue
    "#FFD93D",  # Gold
    "#6BCB77",  # Green
]

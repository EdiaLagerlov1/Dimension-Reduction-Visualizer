"""
Data preparation workflow.
"""
from src.data.csv_reader import read_csv_data
from src.data.vector_io import save_vectors
from src.preprocessing.vectorizer import vectorize_sentences
from src.utils import config
from src.utils.timing import Timer, save_runtime, initialize_runtime_file


def prepare_data():
    """Prepare data: read CSV and vectorize sentences."""
    print("=" * 50)
    print("PREPARING DATA")
    print("=" * 50)

    # Initialize runtime file
    initialize_runtime_file(config.OUTPUT_RUNTIME_PATH)
    print(f"Runtime log: {config.OUTPUT_RUNTIME_PATH}\n")

    # Read CSV
    print(f"Reading CSV from: {config.INPUT_CSV_PATH}")
    sentences, categories = read_csv_data(config.INPUT_CSV_PATH)
    print(f"Loaded {len(sentences)} sentences from {len(set(categories))} categories")

    # Vectorize
    print("Vectorizing sentences using Word2Vec...")
    with Timer() as timer:
        vectors = vectorize_sentences(sentences)
    print(f"Generated vectors of shape: {vectors.shape}")

    # Save runtime
    save_runtime(timer.elapsed(), "Word2Vec Vectorization", config.OUTPUT_RUNTIME_PATH)

    # Save vectors
    save_vectors(vectors, categories, config.OUTPUT_VECTORS_PATH)
    print(f"Vectors saved to: {config.OUTPUT_VECTORS_PATH}")
    print("Data preparation complete!\n")

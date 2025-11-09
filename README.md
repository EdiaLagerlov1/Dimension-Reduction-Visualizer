# Dimension Reduction Visualizer

A modular Python application for text sentence vectorization and 3D dimension reduction visualization using PCA and t-SNE, with comprehensive runtime tracking and aligned results.

## Features

- **Data Preparation**: Convert sentences to vectors using Word2Vec
- **PCA (NumPy)**: Pure NumPy implementation using eigendecomposition
- **PCA (Scikit-learn)**: Scikit-learn implementation using SVD
- **PCA Alignment**: Both PCA results aligned for direct comparison
- **t-SNE**: 3D t-SNE visualization using scikit-learn
- **Runtime Tracking**: Automatic performance metrics for all operations
- **Dynamic Colors**: Automatic color assignment for any categories
- **Modular Design**: Run each step independently via CLI

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Prepare Data Only
```bash
python main.py --prepare
```
**Reads** `input/sentences.csv`, converts sentences to vectors
**Outputs**:
- `output/vectors.txt` - Word2Vec vectors (100D)
- `output/runtime.txt` - Vectorization runtime

### Run PCA (Both Implementations)
```bash
python main.py --pca
```
**Outputs**:
- `output/PCA_numpy.png` - NumPy PCA visualization
- `output/PCA_sklearn.png` - Sklearn PCA visualization (aligned)
- `output/PCA_numpy_vectors.txt` - NumPy 3D vectors
- `output/PCA_sklearn_vectors.txt` - Sklearn 3D vectors (aligned)
- `output/runtime.txt` - PCA runtime statistics (appended)

### Run t-SNE
```bash
python main.py --tsne
```
**Outputs**:
- `output/Tsne.png` - t-SNE visualization
- `output/runtime.txt` - t-SNE runtime statistics (appended)

### Run All Steps
```bash
python main.py --all
```
Executes data preparation, both PCA implementations, and t-SNE in sequence.

## Output Files

After running `python main.py --all`, you'll get:

```
output/
├── vectors.txt                 # Word2Vec vectors (100D)
├── PCA_numpy.png               # NumPy PCA 3D visualization
├── PCA_sklearn.png             # Sklearn PCA 3D visualization (aligned)
├── Tsne.png                    # t-SNE 3D visualization
├── PCA_numpy_vectors.txt       # NumPy PCA 3D coordinates
├── PCA_sklearn_vectors.txt     # Sklearn PCA 3D coordinates (aligned)
└── runtime.txt                 # Consolidated performance log
```

## Visualizations

### PCA (NumPy Implementation)
![PCA NumPy](output/PCA_numpy.png)

### PCA (Scikit-learn Implementation - Aligned)
![PCA Sklearn](output/PCA_sklearn.png)

### t-SNE Visualization
![t-SNE](output/Tsne.png)

## Sample Output Content

### Runtime Log (runtime.txt)
```
==================================================
DIMENSION REDUCTION VISUALIZER - RUNTIME LOG
==================================================
Generated: 2025-11-09 15:30:45

Word2Vec Vectorization
--------------------------------------------------
Time: 1.2345 seconds
Time: 0.0206 minutes

PCA (NumPy)
--------------------------------------------------
Time: 0.0123 seconds
Time: 0.0002 minutes

PCA (Scikit-learn)
--------------------------------------------------
Time: 0.0089 seconds
Time: 0.0001 minutes

t-SNE
--------------------------------------------------
Time: 3.4567 seconds
Time: 0.0576 minutes
```

### Word2Vec Vectors (vectors.txt - sample)
```
Positive: [0.045123, -0.123456, 0.234567, ..., 0.789012]
Neutral: [-0.012345, 0.345678, -0.456789, ..., -0.123456]
Negative: [0.234567, -0.567890, 0.678901, ..., 0.345678]
...
```

### PCA 3D Vectors (PCA_numpy_vectors.txt - sample)
```
Positive: [-2.345678, 1.234567, 0.567890]
Neutral: [0.123456, -0.234567, -0.890123]
Negative: [3.456789, -1.567890, 0.234567]
...
```

## Project Structure

```
├── input/
│   └── sentences.csv               # Input CSV with sentences and categories
├── output/                         # Generated visualizations and data
├── src/
│   ├── data/                       # Data layer
│   │   ├── csv_reader.py          # CSV file reading
│   │   └── vector_io.py           # Vector save/load operations
│   ├── preprocessing/              # Data preprocessing
│   │   └── vectorizer.py          # Word2Vec conversion
│   ├── reduction/                  # Dimension reduction algorithms
│   │   ├── pca_numpy.py           # NumPy PCA implementation
│   │   ├── pca_sklearn.py         # Sklearn PCA implementation
│   │   └── tsne.py                # t-SNE implementation
│   ├── visualization/              # Plotting utilities
│   │   └── plotter.py             # 3D visualization with dynamic colors
│   ├── workflows/                  # Workflow orchestration
│   │   ├── prepare.py             # Data preparation workflow
│   │   ├── pca_workflow.py        # PCA workflow with alignment
│   │   └── tsne_workflow.py       # t-SNE workflow
│   └── utils/                      # Shared utilities
│       ├── config.py              # Configuration constants
│       ├── validators.py          # Input validation
│       ├── alignment.py           # PCA component alignment
│       ├── timing.py              # Runtime tracking
│       └── colors.py              # Dynamic color mapping
├── main.py                         # CLI entry point
├── requirements.txt                # Dependencies
├── README.md                       # This file
└── prd.md                          # Product Requirements Document
```

## Input Format

CSV file with `category` and `sentence` columns:

```csv
category,sentence
Positive,"Great product exceeded expectations"
Neutral,"Average quality meets expectations"
Negative,"Poor quality disappointed"
```

**Note**: Any number of categories is supported - colors are assigned automatically!

## Sample Dataset

The included `input/sentences.csv` contains:
- 600 sentences
- 3 categories: Positive, Neutral, Negative
- Realistic product review text

## Key Features Explained

### PCA Alignment
Both PCA implementations are mathematically equivalent but may differ in sign/orientation. The sklearn implementation is automatically aligned to match the numpy implementation for direct visual comparison.

### Dynamic Color Assignment
Categories are automatically assigned distinct colors from a 10-color palette:
- Colors remain consistent across all visualizations
- Same category = same color in PCA and t-SNE plots
- Works with any number of categories (colors cycle if >10)

### Runtime Tracking
All major operations are timed automatically:
- Word2Vec vectorization
- PCA (NumPy)
- PCA (Scikit-learn)
- t-SNE
Results saved to `output/runtime.txt` with timestamps.

## Architecture Principles

- **Maximum 100 lines per file**: Strict file size limit maintained
- **Single Responsibility**: Each module does one thing
- **No Code Duplication**: Shared logic in utilities
- **Separation of Concerns**: Data/logic/presentation separated

## Configuration

Modify `src/utils/config.py` to adjust:

**Word2Vec Parameters**:
- Vector size, window, epochs, etc.

**Dimension Reduction Parameters**:
- Number of components (3 for 3D)
- t-SNE perplexity and iterations

**Visualization Parameters**:
- Figure size, point size, alpha
- Color palette

## Technical Details

- **Python**: 3.8+
- **PCA (NumPy)**: Covariance matrix eigendecomposition
- **PCA (Sklearn)**: SVD-based (more numerically stable)
- **t-SNE**: Scikit-learn implementation
- **Word2Vec**: Gensim library

## Performance Notes

Typical runtimes on sample dataset (600 sentences):
- Word2Vec vectorization: ~1-2 seconds
- PCA (NumPy): <0.1 seconds
- PCA (Sklearn): <0.1 seconds
- t-SNE: ~3-5 seconds

Check `output/runtime.txt` for actual performance on your machine.

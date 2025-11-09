# Product Requirements Document (PRD)
## Dimension Reduction Visualizer

### 1. Project Overview
A modular Python application that processes text sentences, converts them to vectors, and visualizes dimension reduction using PCA and t-SNE techniques with comprehensive runtime tracking and aligned results.

### 2. Core Features

#### 2.1 Data Preparation Module
- **Input**: CSV file with sentences and categories (from `input/` folder)
- **Process**: Convert sentences to vectors using Word2Vec
- **Output**:
  - Word2Vec vectors saved as text file in `output/` folder
  - Runtime statistics logged to `runtime.txt`
- **Execution**: Standalone execution via CLI

#### 2.2 PCA Visualization Module (NumPy Implementation)
- **Input**: Pre-processed vector data
- **Process**: Calculate 3D PCA using NumPy eigendecomposition
- **Output**:
  - 3D visualization saved as `PCA_numpy.png`
  - 3D PCA vectors saved as `PCA_numpy_vectors.txt`
  - Runtime statistics logged to `runtime.txt`
- **Execution**: Standalone execution via CLI

#### 2.3 PCA Visualization Module (Scikit-learn Implementation)
- **Input**: Pre-processed vector data
- **Process**: Calculate 3D PCA using sklearn SVD
- **Alignment**: Components aligned to NumPy PCA for direct comparison
- **Output**:
  - 3D visualization saved as `PCA_sklearn.png`
  - 3D PCA vectors saved as `PCA_sklearn_vectors.txt`
  - Runtime statistics logged to `runtime.txt`
- **Execution**: Standalone execution via CLI

#### 2.4 t-SNE Visualization Module
- **Input**: Pre-processed vector data
- **Process**: Calculate 3D t-SNE using sklearn
- **Output**:
  - 3D visualization saved as `Tsne.png`
  - Runtime statistics logged to `runtime.txt`
- **Execution**: Standalone execution via CLI

#### 2.5 Runtime Tracking
- **Feature**: All computations are timed automatically
- **Output**: Consolidated `runtime.txt` with timestamps and performance metrics
- **Includes**: Word2Vec vectorization, PCA (NumPy), PCA (Sklearn), t-SNE

#### 2.6 Dynamic Color Assignment
- **Feature**: Categories automatically assigned distinct colors
- **Consistency**: Same category has same color across all visualizations
- **Scalability**: Supports any number of categories via color palette cycling

### 3. Technical Requirements

#### 3.1 Architecture Principles
- **Maximum file length**: 100 lines per file (strict)
- **Single Responsibility**: Each module performs ONE function
- **No duplicate code**: Shared logic in utility modules
- **Separation of Concerns**: Data/logic/presentation layers separated

#### 3.2 Technology Stack
- **Language**: Python 3.8+
- **Core Libraries**:
  - gensim (Word2Vec)
  - numpy (PCA implementation, numerical operations)
  - scikit-learn (PCA, t-SNE)
  - matplotlib (3D visualization)
  - pandas (CSV handling)

### 4. Project Structure

```
project/
├── input/                          # Input data folder
│   └── sentences.csv               # CSV with sentences and categories
├── output/                         # Output folder for results
│   ├── vectors.txt                 # Word2Vec vectors (100D)
│   ├── PCA_numpy.png               # NumPy PCA visualization
│   ├── PCA_sklearn.png             # Sklearn PCA visualization (aligned)
│   ├── Tsne.png                    # t-SNE visualization
│   ├── PCA_numpy_vectors.txt       # NumPy PCA 3D vectors
│   ├── PCA_sklearn_vectors.txt     # Sklearn PCA 3D vectors (aligned)
│   └── runtime.txt                 # Consolidated runtime log
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
│   ├── visualization/              # Plotting layer
│   │   └── plotter.py             # 3D visualization utilities
│   ├── workflows/                  # Workflow orchestration
│   │   ├── prepare.py             # Data preparation workflow
│   │   ├── pca_workflow.py        # PCA workflow with alignment
│   │   └── tsne_workflow.py       # t-SNE workflow
│   └── utils/                      # Shared utilities
│       ├── config.py              # Configuration constants
│       ├── validators.py          # Input validation
│       ├── alignment.py           # PCA component alignment
│       ├── timing.py              # Runtime tracking utilities
│       └── colors.py              # Dynamic color mapping
├── main.py                         # CLI entry point
├── requirements.txt                # Dependencies
├── README.md                       # User documentation
└── prd.md                          # This document
```

### 5. Functional Requirements

#### 5.1 CLI Interface
```bash
# Prepare data only
python main.py --prepare

# Run PCA (both implementations with alignment)
python main.py --pca

# Run t-SNE
python main.py --tsne

# Run all steps
python main.py --all
```

#### 5.2 Data Format Specifications

**Input CSV Format**:
```
category,sentence
Positive,"Great product exceeded expectations"
Neutral,"Average quality meets expectations"
Negative,"Poor quality disappointed"
```

**Output Vector Format** (vectors.txt):
```
Positive: [0.123456, 0.234567, ..., 0.789012]
Neutral: [0.234567, 0.345678, ..., 0.890123]
Negative: [0.345678, 0.456789, ..., 0.901234]
```

**Runtime Log Format** (runtime.txt):
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

### 6. Non-Functional Requirements

- **Modularity**: Each step runs independently
- **Reusability**: Common code extracted to utilities
- **Readability**: Clear function/variable names, docstrings
- **Error Handling**: Validate inputs, handle missing files
- **Performance**: Efficient vector operations using NumPy
- **Consistency**: Aligned PCA results for direct comparison
- **Observability**: Comprehensive runtime tracking
- **Flexibility**: Dynamic color assignment for any categories

### 7. Implementation Details

#### 7.1 PCA Alignment Algorithm
- NumPy PCA serves as reference implementation
- Sklearn PCA components aligned using correlation-based sign flipping
- Ensures both visualizations are directly comparable
- Implementation in `src/utils/alignment.py`

#### 7.2 Color Assignment Strategy
- 10-color palette for visual distinction
- Categories sorted alphabetically for consistency
- Colors cycle for datasets with >10 categories
- Same category → same color across all visualizations
- Implementation in `src/utils/colors.py`

#### 7.3 Runtime Tracking
- Context manager pattern for accurate timing
- Single consolidated log file with timestamps
- Separate entries for each major operation
- Implementation in `src/utils/timing.py`

### 8. Success Criteria

- [x] All files under 100 lines
- [x] Each module has single responsibility
- [x] No code duplication across modules
- [x] Data preparation runs standalone
- [x] PCA (NumPy) runs standalone and produces visualization
- [x] PCA (sklearn) runs standalone and produces visualization
- [x] t-SNE runs standalone and produces visualization
- [x] All visualizations saved correctly to output folder
- [x] Clean separation between data/logic/presentation layers
- [x] PCA implementations aligned for comparison
- [x] Runtime tracking for all operations
- [x] Dynamic color assignment for any categories
- [x] Vector outputs saved for both PCA implementations

### 9. Configuration Parameters

All configurable parameters in `src/utils/config.py`:

**Word2Vec Parameters**:
- Vector Size: 100
- Window: 5
- Min Count: 1
- Epochs: 100

**Dimension Reduction Parameters**:
- Components: 3 (for 3D visualization)
- t-SNE Perplexity: 10
- t-SNE Iterations: 1000

**Visualization Parameters**:
- Figure Size: (10, 8)
- Point Size: 50
- Alpha: 0.7
- Color Palette: 10 distinct colors

### 10. Sample Dataset

Included `input/sentences.csv` with:
- 600 sentences
- 3 categories (Positive, Neutral, Negative)
- Realistic product review text
- Suitable for testing and demonstration

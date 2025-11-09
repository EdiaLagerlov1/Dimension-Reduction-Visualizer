# Project Prompts
## Dimension Reduction Visualizer

This file contains the prompts used to create this project.

---

## Prompt 1: Initial Project Setup

**Date**: Initial Implementation

**Prompt**:

```
You are a software architect, Please create prd.md to the task below
Please follow:
- **Maximum file length**: 100 lines per file (strict limit)
- **Single Responsibility**: Each file/class/function does ONE thing
- **No duplicate code**: Extract common logic into reusable functions
- **Separation of Concerns**: Separate data, business logic, and presentation


Get sentences, divided to the 3 categories from csv file under folder: input
prepare the data by converting the sentences to vectors using word2vec and save it as a lists text file under folder:output
Calc the PCA (3D)  using numpy
Display visualization of the PCA results and save it as "PCA_numpy"  under: output
Calc the PCA (3D)  using sklearn
Display visualization of the PCA results and save it as "PCA_sklearn" under: output
Calc the T-sne (3D)  using any liberary
Display visualization of the PCA results  and save it as "Tsne" under: output
Please let the user to run prepare data, pca and tsne separately
```

**Outcome**:
- Created comprehensive PRD (Product Requirements Document)
- Implemented complete modular project structure
- All files under 100 lines
- Separation of concerns maintained
- CLI interface for independent execution of each step

**Key Features Implemented**:
1. ✅ Data preparation with Word2Vec
2. ✅ PCA implementation using NumPy (eigendecomposition)
3. ✅ PCA implementation using Scikit-learn (SVD)
4. ✅ t-SNE implementation
5. ✅ 3D visualizations for all methods
6. ✅ Independent execution via CLI flags
7. ✅ Modular architecture with utilities

---

## Prompt 2: Documentation and Analysis

**Date**: Final Documentation Phase

**Prompt**:

```
1. Pls align the readme with the final code and add the display the output pictures itself in it

2. can you create file "ניתוח תוצאות-הסבר" in hebrew, with what was done and final conclusions,
   pls display the output pictures itself in it
```

**Outcome**:
1. **README.md Updated**:
   - Added embedded visualizations using markdown image syntax
   - Added sample output content (runtime logs, vectors)
   - Aligned with final implementation
   - Complete usage examples and explanations

2. **ניתוח תוצאות-הסבר.md Created** (Hebrew Analysis):
   - Comprehensive analysis of the entire process
   - Detailed explanation of each algorithm
   - Embedded visualizations with analysis
   - Performance comparisons
   - Conclusions and recommendations
   - Complete in Hebrew language

**Additional Features Added During Development**:
1. ✅ PCA alignment (sklearn aligned to numpy for comparison)
2. ✅ Runtime tracking for all operations
3. ✅ Dynamic color assignment for any number of categories
4. ✅ Vector outputs saved for both PCA implementations
5. ✅ Consolidated runtime log file
6. ✅ Comprehensive error handling and validation

---

## Evolution of Requirements

### Initial Requirements:
- Basic data preparation
- Two PCA implementations
- One t-SNE implementation
- Separate execution capability

### Final Implementation Includes:
1. **Enhanced Data Processing**:
   - Word2Vec vectorization with configurable parameters
   - Vector I/O utilities for saving/loading
   - CSV validation and error handling

2. **Advanced PCA Features**:
   - NumPy implementation (eigendecomposition)
   - Scikit-learn implementation (SVD)
   - Automatic alignment between implementations
   - Both implementations save 3D vectors

3. **Performance Tracking**:
   - Timer utility for all operations
   - Consolidated runtime log with timestamps
   - Performance comparison data

4. **Visualization Enhancements**:
   - Dynamic color palette (supports unlimited categories)
   - Consistent colors across all visualizations
   - High-quality 3D scatter plots with legends
   - Black edge highlighting for better visibility

5. **Documentation**:
   - Comprehensive PRD
   - User-friendly README with embedded images
   - Hebrew analysis document with detailed explanations
   - Sample data included (600 sentences, 3 categories)

6. **Code Quality**:
   - All files under 100 lines (strict adherence)
   - Single responsibility principle
   - No code duplication
   - Clean separation of concerns
   - Workflow orchestration layer added

---

## Architecture Decisions

### Why Workflows Folder?
- Main.py exceeded 100 lines
- Solution: Extract each workflow to separate file
- Result: prepare.py, pca_workflow.py, tsne_workflow.py
- Each workflow orchestrates its specific process

### Why Alignment Utility?
- PCA implementations may differ in sign/orientation
- Solution: Correlation-based sign flipping
- Result: Direct visual comparison possible
- Helps validate NumPy implementation

### Why Timing Utility?
- Need performance metrics for all operations
- Solution: Context manager (Timer class)
- Result: Clean, reusable timing code
- Single consolidated log file

### Why Colors Utility?
- Need consistent colors across visualizations
- Solution: Dynamic color mapping from sorted categories
- Result: Works with any number of categories
- 10-color palette with cycling

---

## Lessons Learned

1. **100-Line Limit**: Enforces modularity and clean code
2. **Single Responsibility**: Makes code easier to test and maintain
3. **Separation of Concerns**: Clear boundaries between layers
4. **Reusable Utilities**: Saves time and reduces bugs
5. **Progressive Enhancement**: Started simple, added features incrementally

---

## Future Enhancements (Not Implemented)

Potential improvements for future versions:
- Interactive 3D plots (using Plotly)
- Support for more dimension reduction algorithms (UMAP, LLE, etc.)
- Batch processing for multiple CSV files
- Export to different formats (JSON, Pickle, etc.)
- Web interface for easier usage
- GPU acceleration for large datasets
- Automated hyperparameter tuning

---

## File Structure Evolution

**Initial Plan**:
```
src/
├── data/
├── preprocessing/
├── reduction/
├── visualization/
└── utils/
```

**Final Structure** (with additions):
```
src/
├── data/              # Data I/O operations
├── preprocessing/     # Word2Vec vectorization
├── reduction/         # PCA (NumPy, Sklearn), t-SNE
├── visualization/     # 3D plotting with dynamic colors
├── workflows/         # Orchestration (NEW)
└── utils/             # Config, validators, alignment, timing, colors (EXPANDED)
```

---

**Project Completion Date**: November 2025
**Total Development Iterations**: Multiple refinements based on feedback
**Final Status**: ✅ Complete and Fully Functional

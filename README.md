# Year 3 Project: ML-based Network Attack Detection and Explanation

Repository for the Year 3 project focused on machine learning-based detection and explanation of network attacks, specifically targeting botnet variants.

## Quick Start

- **Prerequisites**: Python 3.12, IDE for Python and Jupyter (e.g., VS Code)
- **Install Dependencies**: `pip install -r requirements.txt`
- **Datasets**:
  - CTU-13: [Download](https://github.com/imfaisalmalik/CTU13-CSV-Dataset)
  - CICIDS2017: [Download](http://205.174.165.80/CICDataset/CIC-IDS-2017/) (Use CSVs in `ML` directory)
- **Run Pre-processing Scripts**: Start with `relabelCTU13.py`
- **Run Notebooks**: Start with `trainDummyClassifier.ipynb` 

## Structure

### Codebase

Includes scripts and Jupyter notebooks for preprocessing, training models, and visualizing results:

- `relabelCTU13.py` & `relabelCICIDS2017.py`: Relabel datasets for consistency.
- `trainDummyClassifier.ipynb`: Baseline model training.
- `trainRandomForest.ipynb` & `trainSVM.ipynb`: Train RandomForest and SVM classifiers.
- `plotData.py`: Visualize dataset statistics and results.

### Directory Organization

- **Root**: Contains all source code files.
- **Subdirectories**:
  - `CTU13`: CTU-13 dataset files.
  - `CICIDS2017`: CICIDS2017 dataset files.

### Environment Setup

Ensure your environment is set up with the required dependencies:

- **IDE**: Supports Python and Jupyter notebooks.
- **Python**: Version 3.12.x.
- **Packages**: pandas (2.2.1), numpy (1.26.4), scikit-learn (1.4.1.post1), shap (0.45.0), matplotlib (3.8.3), ipywidgets (8.1.2).

## Running the Project

1. Install all dependencies listed in `requirements.txt`.
2. Download and prepare datasets as outlined.
3. Execute the notebooks in the order provided to train models and evaluate their performance.

## Notes

- CTU-13 dataset is pre-formatted. For CICIDS2017, ensure to use CSV files from the `ML` directory post-download.

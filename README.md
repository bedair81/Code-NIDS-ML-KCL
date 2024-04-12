# Year 3 Project: Transferability and Explainability of Machine Learning Models for Network Intrusion Detection

Repository for the Year 3 project focused on machine learning-based detection and explanation of network attacks, specifically targeting botnet variants.

## Quick Start

- **Prerequisites**: 
  - IDE that can run Python and Jupyter notebooks (e.g., Visual Studio Code with the necessary extensions).
  - Python version 3.10.14 (specifically, any 3.10.x version should suffice).
  - A Nvidia GPU with CUDA support for running the CUML models.
  - A valid RAPIDS AI environment. Follow the installation instructions at [RAPIDS AI](https://docs.rapids.ai/install), choosing the RAPIDS version 24.02 with the CUDA 12 option.

- **Install Dependencies**: 
  ```
  conda install pandas=2.2.1 numpy=1.26.4 shap=0.45.0 matplotlib=3.8.3 ipywidgets=8.1.2
  ```
  
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
- `plotData.ipynb`: Visualize dataset statistics and results.

### Directory Organization

- **Root**: Contains all source code files.
- **Subdirectories**:
  - `CTU13`: CTU-13 dataset files.
  - `CICIDS2017`: CICIDS2017 dataset files.

### Environment Setup

Ensure your environment is set up with the required dependencies:

- **IDE**: Supports Python and Jupyter notebooks.
- **Python**: Version 3.10.14 (any 3.10.x version should suffice).
- **Packages** (compatible versions are listed):
  - pandas (2.2.1)
  - numpy (1.26.4)
  - cuml (24.02)
  - shap (0.45.0)
  - matplotlib (3.8.3)
  - ipywidgets (8.1.2)

## Running the Project

1. Set up the directory structure and install the necessary packages as mentioned in the Environment Setup section.
2. Download and prepare datasets as outlined.
3. Execute the code files in the order listed in the Codebase section to preprocess the datasets, train classifiers, evaluate their performance, and generate visualizations of the data and results.

## Notes

- The CTU-13 CSV files are provided in the correct format. For CICIDS2017, download the dataset and use the CSV files in the `ML` directory.
- Due to the extensive training times required for the CPU-based models, we switched to CUML's GPU-accelerated models. Ensure that you have a compatible Nvidia GPU and the necessary RAPIDS AI environment set up to run these models.
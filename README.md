# Year 3 Project: Transferability and Explainability of Machine Learning Models for Network Intrusion Detection

This repository is dedicated to the Year 3 project on the use of machine learning for detecting and explaining network intrusions, with a focus on botnet variations.

## Quick Start Guide

### Prerequisites:
- **IDE**: Any IDE capable of running Python and Jupyter notebooks, such as Visual Studio Code with appropriate extensions.
- **Python**: Version 3.10.14 or any 3.10.x version.
- **Hardware**: Nvidia GPU with CUDA support for executing CUML models.
- **Environment**: RAPIDS AI environment, installable following instructions at [RAPIDS AI](https://docs.rapids.ai/install) for version 24.02 with CUDA 12.

### Installation of Dependencies:
```bash
conda install pandas=2.2.1 numpy=1.26.4 shap=0.45.0 matplotlib=3.8.3 ipywidgets=8.1.2
```

### Datasets:
- **CTU-13**: [Download here](https://github.com/imfaisalmalik/CTU13-CSV-Dataset)
- **CICIDS2017**: [Download here](http://205.174.165.80/CICDataset/CIC-IDS-2017/) (Use the CSVs in the `ML` directory)

### Initial Steps:
- Start by running `relabelCTU13.py` to preprocess the data.
- Proceed with the Jupyter notebook `trainDummyClassifier.ipynb` for initial model training.

## Project Structure

### Codebase
Includes scripts and notebooks for data preprocessing, model training, and result visualization:
- `relabelCTU13.py` & `relabelCICIDS2017.py`: Scripts for relabeling datasets.
- `trainDummyClassifier.ipynb`: Notebook for baseline model training.
- `trainRandomForest.ipynb` & `trainSVM.ipynb`: Notebooks for training RandomForest and SVM classifiers.
- `plotData.ipynb`: Notebook for visualizing dataset statistics and outcomes.

### Directory Layout
- **Root**: Main source code directory.
- **Subdirectories**:
  - `CTU13`: Files related to the CTU-13 dataset.
  - `CICIDS2017`: Files for the CICIDS2017 dataset.

### Environment Setup
Ensure the setup includes all necessary dependencies:
- **IDE Support**: Compatible with Python and Jupyter notebooks.
- **Python Version**: 3.10.14 (or any 3.10.x).
- **Required Packages**:
  - pandas (2.2.1)
  - numpy (1.26.4)
  - cuml (24.02)
  - shap (0.45.0)
  - matplotlib (3.8.3)
  - ipywidgets (8.1.2)

## Execution Instructions

1. Organize the directory structure and install the required packages as specified in the Environment Setup section.
2. Download and prepare the datasets as described.
3. Run the scripts and notebooks in the specified order to preprocess data, train models, assess their effectiveness, and visualize both data and findings.

## Additional Notes

- The CTU-13 dataset is already formatted correctly. For CICIDS2017, ensure to download and utilize the CSV files from the `ML` directory.
- Switch to CUML's GPU-accelerated models to reduce the computation time required for CPU-based models. Verify that your Nvidia GPU and RAPIDS AI environment are appropriately configured.

## Further Information

- **Thesis Documentation**: For comprehensive details on the theoretical framework, research methods, and analysis of the project results, refer to the dissertation available at [Thesis-NIDS-ML-KCL](https://github.com/bedair81/Thesis-NIDS-ML-KCL).
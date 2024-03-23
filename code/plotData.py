# Random Forest
rf_acc_ctu13_bin = 0.997235
rf_f1_ctu13_bin = 0.996723
rf_acc_cicids_bin = 0.989733
rf_f1_cicids_bin = 0.974258
rf_acc_cicids_multi = 0.989428
rf_f1_cicids_multi = 0.816561

# SVM
svm_acc_ctu13_bin = 0.873228
svm_f1_ctu13_bin = 0.846285
svm_acc_cicids_bin = 0.774821
svm_f1_cicids_bin = 0.231026
svm_acc_cicids_multi = 0.804313
svm_f1_cicids_multi = 0.135484

import matplotlib.pyplot as plt
import numpy as np

# Define the labels and width of the bars
labels = ['CTU13 Binary', 'CICIDS2017 Binary', 'CICIDS2017 Multiclass']
width = 0.35

# Set the positions of the bars on the x-axis
x = np.arange(len(labels))

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create the bars for Random Forest
rf_acc = [rf_acc_ctu13_bin, rf_acc_cicids_bin, rf_acc_cicids_multi]
rf_f1 = [rf_f1_ctu13_bin, rf_f1_cicids_bin, rf_f1_cicids_multi]
ax.bar(x - width/2, rf_acc, width, label='Random Forest Accuracy')
ax.bar(x - width/2, rf_f1, width, bottom=rf_acc, label='Random Forest F1-score')

# Create the bars for SVM
svm_acc = [svm_acc_ctu13_bin, svm_acc_cicids_bin, svm_acc_cicids_multi]
svm_f1 = [svm_f1_ctu13_bin, svm_f1_cicids_bin, svm_f1_cicids_multi]
ax.bar(x + width/2, svm_acc, width, label='SVM Accuracy')
ax.bar(x + width/2, svm_f1, width, bottom=svm_acc, label='SVM F1-score')

# Add labels and title
ax.set_xlabel('Dataset')
ax.set_ylabel('Score')
ax.set_title('Performance Comparison: Random Forest vs SVM')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Display the graph
plt.tight_layout()
plt.show()
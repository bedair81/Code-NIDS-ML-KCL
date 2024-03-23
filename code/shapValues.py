import pickle
import shap
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Load the trained classifier from the pickle file
with open('trained_classifier.pkl', 'rb') as file:
    classifier = pickle.load(file)

# Prepare the CTU13 dataset for testing
X_test = test_ctu13[features]
y_test = test_ctu13['GT']

# Make predictions on the CTU13 dataset
predictions = classifier.predict(X_test)

# Compute SHAP values
explainer = shap.Explainer(classifier, X_test)
shap_values = explainer(X_test)

# Visualize the SHAP values
shap.summary_plot(shap_values, X_test, plot_type="bar", feature_names=features)
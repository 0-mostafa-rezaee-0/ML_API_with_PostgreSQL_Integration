import logging
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import pickle
import os

# Configure logging before doing anything else
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Get the project root directory (one level up from scripts)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Save the model using absolute path
model_path = os.path.join(PROJECT_ROOT, 'models', 'ml_model.pkl')
pickle.dump(model, open(model_path, 'wb'))

# Log important messages
logging.info(f"Model Accuracy: {accuracy:.2f}")
logging.info("Model saved as ml_model.pkl")

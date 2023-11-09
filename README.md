# Diabetes_Prediction

## workflow: 

### Imports necessary libraries:

streamlit as st for creating the web application.
pandas for data manipulation.
DecisionTreeClassifier from sklearn.tree for building a classification model.
train_test_split from sklearn.model_selection for splitting the dataset.
metrics from sklearn for evaluating the model.
OrdinalEncoder from sklearn.preprocessing for encoding categorical data.
numpy as np for numerical operations.

### Procedure
It reads a CSV file containing diabetes-related data using Pandas and stores it in the file variable.

It uses an OrdinalEncoder to encode the 'gender' and 'smoking_history' columns in the dataset.

It separates the features ('x') and the target ('y') for the model.

It splits the data into training and testing sets using train_test_split.

A decision tree classifier is trained on the training data.

The model is used to make predictions on the testing data.

The Streamlit app is configured with a title, icon, and layout settings.

A header with the title "Diabetes Prediction" is displayed.

Two columns are created using st.columns(2) for user input and result display. In the left column (col1), the user can input information, and in the right column (col2), the result will be displayed.

Within col1, the user is asked to input their gender, hypertension status, heart disease status, and smoking history using select boxes. The values are mapped to numerical values using dictionaries.

Within col2, the user is asked to input their age, BMI, HbA1c level, and blood glucose level using text input fields.

Three more columns (a, b, and c) are created to format the layout of the "Submit" button.

In col2, a "Submit" button is displayed. When the button is pressed, the data provided by the user is collected and formatted as an array. The model is then used to predict whether the user has diabetes or not based on the provided inputs.

If the model predicts diabetes (1), an error message is displayed. If not, a success message is displayed, indicating that the user is healthy.

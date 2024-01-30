# Author: Your Name
# Project: Smell Sensing Model Version 1 - Data Acquisition and Neural Network Training

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import regularizers
from sklearn.model_selection import train_test_split
import pandas as pd
import glob

# Function to load data from CSV files
def load_data_from_csv():
    # Get a list of all CSV files
    files = glob.glob('E:/BACKGROUNDdata_*.csv')  # replace 'E:\\' with your USB drive's path
    
    # Read the CSV files into a DataFrame
    data = pd.concat([pd.read_csv(file) for file in files])
    
    # Split the data into X and y
    X = data.drop('Temperature', axis=1)
    y = data['Temperature']
    
    return X, y

# Load the data
X, y = load_data_from_csv()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],), kernel_regularizer=regularizers.l1_l2(l1=1e-5, l2=1e-4)),
    Dense(32, activation='relu', kernel_regularizer=regularizers.l1_l2(l1=1e-5, l2=1e-4)),
    Dense(1, activation='sigmoid'),
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Save the model
model.save('my_model.h5')

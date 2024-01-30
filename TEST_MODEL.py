# Author: Aditya Sharma
# Project: Smell Sensing Model Version 1 - Data Transfer and Prediction
import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import serial
import time

# Load the trained model
model = load_model("")

# Establish communication with Arduino
ser = serial.Serial('COM9', 9600)
time.sleep(2)

# Define the means and standard deviations for normalization
means = np.array([36.6395, 2.9867, 123.5196, 2.9867, 54.1952, 28.449, 242.1697, 22.4664])
std_devs = np.array([8.0384, 1.0675, 290.0955, 1.0675, 5.6318, 16.2025, 238.1397, 4.8474])

# Continuously read data from Arduino and make predictions
while True:
    try:
        # Read 8 lines from the serial port
        lines = [ser.readline().decode('utf-8').strip() for _ in range(10)][1:]
        
        # Convert the lines to a DataFrame
        data = pd.DataFrame([[float(x) for x in line.split(',')] for line in lines])
        
        # Normalize the data
        data = (data - means) / std_devs
        
        # Make a prediction using the model
        prediction = model.predict(data)
        
        # Print the prediction
        print(f'Prediction: {prediction}')
    except KeyboardInterrupt:
        # Break the loop if there is a KeyboardInterrupt
        break

# Close the serial port
ser.close()

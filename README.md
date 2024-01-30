# Smell Sensing Model Version 1

## Author
Aditya Sharma

## Introduction
This project involves the creation of a smell sensing model using various gas sensors. The data from these sensors is collected using an Arduino-based system and stored in CSV files. This data is then used to train a neural network for smell identification tasks.

## Sensors Used
- DHT11 for temperature and humidity
- MQ-3 for ethanol detection
- MQ-2 for LPG and propane detection
- MQ-4 for methane and natural gas detection
- MQ-8 for hydrogen detection
- A VOC sensor for volatile organic compound detection

## Data Acquisition
The data from the sensors is read using an Arduino UNO. The sensor readings are written to CSV files, with each file containing 10 readings. The code for this part can be found in `data_acquisition.ino`.

## Data Processing and Model Training
The data from the CSV files is loaded into a Python script, where it is split into features and target variables. The data is then split into training and testing sets. A neural network model is defined and trained on the training data. The model includes L1 and L2 regularization to prevent overfitting. The code for this part can be found in `model_training.py`.

## Installation
To run the project, you will need to have the following installed:
- Arduino IDE
- Python 3
- TensorFlow
- Keras
- scikit-learn
- pandas

## Usage
1. Upload the `data_acquisition.ino` sketch to your Arduino UNO.
2. Run the `model_training.py` script in Python.

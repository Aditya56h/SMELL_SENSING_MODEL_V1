# Author: Aditya Sharma
# Project: Smell Sensing Model Version 1 - Data Acquisition and Storage

import serial
import csv
import datetime

# Function to write data to a CSV file
def write_to_csv(filename, data, fieldnames):
    # Open the file in append mode
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        # Create a CSV writer
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write the header if the file is empty
        if file.tell() == 0:
            writer.writeheader()
        
        # Write the data row
        writer.writerow(data)

# Main function
def main():
    # Establish communication with Arduino
    ser = serial.Serial('COM9', 9600)
    
    count = 0
    file_num = 1
    
    # Define the fieldnames for the CSV file
    fieldnames = ['Alcohol PPM', 'LPG GAS', 'CH4 PPM', 'Propane', 'H2PPM', 'Humidity', 'VOC', 'Temperature']
    
    # Continuously read data from Arduino
    while True:
        if ser.inWaiting():
            # Read a line from Arduino and remove trailing whitespace
            line = ser.readline().decode('utf-8').strip()
            
            # Remove commas from the data
            line = line.replace(',', ' ')
            
            # Split the line into values and create a dictionary with the fieldnames
            data = dict(zip(fieldnames, line.split()))
            
            # Define the filename
            filename = f'E:/BACKGROUNDdata_{file_num}.csv'  # replace 'E:\\' with your USB drive's path
            
            # Write the data to the CSV file
            write_to_csv(filename, data, fieldnames)
            
            count += 1
            
            # If 10 lines have been written, start a new file
            if count == 10:
                count = 0
                file_num += 1

# Run the main function
if __name__ == "__main__":
    main()

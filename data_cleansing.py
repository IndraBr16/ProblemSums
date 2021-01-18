# Importing libraries
import pandas as pd
import numpy as np

def readCSV(filename):
    """
    Function that takes in a csv file input and reads it.
    :param filename: Input filename.
    :return: A printing of the first few rows.
    """

    readFile = pd.read_csv(filename)
    return readFile.head()


if __name__ == '__main__':
    hotel_dataset = "hotel_bookings.csv"
    print(readCSV(hotel_dataset))
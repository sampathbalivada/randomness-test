#!/usr/bin/env python3
"""Generates a CSV file with random number frequencies."""

from random import randint
from collections import Counter
import csv

__author__ = "Sampath Balivada"
__copyright__ = "Copyright 2021, Sampath Balivada"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Sampath Balivada"
__email__ = "balivadask2000@gmail.com"

# random number generator
def generate_random_integers(count: int, start_range: int, end_range: int) -> list:
    """ 
    generates and returns count number of random integers in the range 
    [start_range, end_range] using random.randint
    """
    return [randint(start_range, end_range) for _ in range(count)]

# frequency finder
def find_frequency_for_integers(integer_list: list):
    """ 
    returns a Counter object that contains the frequency of occurance of each integer
    """
    return Counter(integer_list)

# store frequency in csv file
def store_frequency(frequency: Counter, start_range: int, end_range: int, file_name: str):
    """ 
    stores the freqiencies in a csv format in the given file
    """
    with open(file_name, 'w', newline="") as output_file:
        csv_writer = csv.writer(output_file)
        for i in range(start_range, end_range+1):
            csv_writer.writerow([i, frequency[i]])

# driver
if __name__ == '__main__':
    random_integers = generate_random_integers(1000000, 0, 100)
    frequency = find_frequency_for_integers(random_integers)
    store_frequency(frequency, 0, 100, "./results/python.csv")
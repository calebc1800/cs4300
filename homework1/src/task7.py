"""
Task 7: Package Management in DevEdu
"""

import numpy as np

def calculate_mean(arr):
    """
    Calculate the mean of a numpy array.
    """
    np_arr = np.array(arr)
    return np.mean(np_arr)


def calculate_sum(arr):
    """
    Calculate the sum of a numpy array.
    """
    np_arr = np.array(arr)
    return np.sum(np_arr)


def calculate_std(arr):
    """
    Calculate the standard deviation of a numpy array.
    """
    np_arr = np.array(arr)
    return np.std(np_arr)

# Simple demonstration when run as script
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    print('Mean:', calculate_mean(data))
    print('Sum:', calculate_sum(data))
    print('Std Dev:', calculate_std(data))

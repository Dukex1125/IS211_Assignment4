import time
import random

my_list = []

def random_list(my_list, list_size):
    """Fills the empty list with random integers.

    Args:
        my_list (list): empty list to be filled with random integers
        list_size (int): value to determine size of list
    Returns:
        my_list (list): list of random value with size determined by list_size value

    Example:
        >>>random_list(my_list, 6)
        [2, 4, 3, 3, 1, 5]
    """

    while len(my_list) < list_size:
        number = random.randint(0, list_size)
        my_list.append(number)

    return my_list

def insertion_sort()

for i in range(100):
    for list_size in (500, 1000, 10000):
        my_list = []
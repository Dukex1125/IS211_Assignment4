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

def sequential_search(my_list, item, list_size):
    """Performs item search on a list and returns bool and string.

    Args"
        my_list (list): list of random integers
        item (int): value used for search on my_list
        list_size (int): value used to determine size of list

    Returns:
        bool: True or False whether item exists in my_list
        str: out of average time on search

    Example:
        >>>sequential_search(my_list, 2, 5)
        (False, 'Sequential Search took 0.0000000 seconds to run on average.
    """

    random_list(my_list, list_size)

    pos = 0
    found = False
    start = time.time()

    while pos < len(my_list) and not found:
        if my_list[pos] == item:
            found = True
        else:
            pos += 1

    end = time.time()

    return found, 'Sequential Search took %10.7f seconds to run, on average.' % (end - start)


def ordered_sequential_search(my_list, item, list_size):
    """Performs item search on an ordered list and returns bool and string.

    Args"
        my_list (list): list of random integers
        item (int): value used for search on my_list
        list_size (int): value used to determine size of list

    Returns:
        bool: True or False whether item exists in my_list
        str: out of average time on search

    Example:
    >>>ordered_sequential_search(my_list, 2, 5)
    (False, 'Ordered Sequential Search took 0.0000000 seconds to run on average.')
    """

    random_list(my_list, list_size)

    pos = 0
    found = False
    stop = False

    new_list = sorted(my_list)

    start = time.time()

    while pos < len(new_list) and not found and not stop:
        if new_list[pos] == item:
            found = True
        elif new_list[pos] > item:
            stop = True
        else:
            pos += 1

    end = time.time()
    return found, "Ordered Sequential Search took %10.7f seconds to run on average." % (end - start)

def binary_search_iterative(my_list, item, list_size):
    """Performs item search on an ordered list and returns bool and string.

    Args"
        my_list (list): list of random integers
        item (int): value used for search on my_list
        list_size (int): value used to determine size of list

    Returns:
        bool: True or False whether item exists in my_list
        str: out of average time on search

    Example:
    >>>binary_search_iterative(my_list, 2, 5)
    (False, 'Ordered Sequential Search took 0.0000000 seconds to run on average.')
    """


    random_list(my_list, list_size)

    first = 0
    last = len(my_list) - 1
    found = False

    new_list = sorted(my_list)

    start = time.time()

    while first <= last and not found:
        midpoint = (first + last) // 2
        if new_list[midpoint] == item:
            found = True
        elif item < new_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    end = time.time()

    return found, 'Binary Search Iterative Search took %10.7f seconds to run, on average.' % (end - start)

def binary_search_recursive(my_list, item, list_size):
    """Performs item search on an ordered list and returns bool and string.

    Args"
        my_list (list): list of random integers
        item (int): value used for search on my_list
        list_size (int): value used to determine size of list

    Returns:
        bool: True or False whether item exists in my_list
        str: out of average time on search

    Example:
    >>>binary_search_recursive(my_list, 2, 5)
    False
    """

    random_list(my_list, list_size)

    new_list = sorted(my_list)

    if len(new_list) == 0:
        return False
    else:
        midpoint = len(new_list) // 2

    if new_list[midpoint] == item:
        return True, 'hi'
    else:
        if item < new_list[midpoint]:
            return binary_search_recursive(new_list[:midpoint], item, midpoint)
        else:
            return binary_search_recursive(new_list[midpoint + 1:], item, midpoint)

for i in range(100):
    for list_size in (500, 1000, 10000):
        print sequential_search(my_list, -1, list_size)
        print ordered_sequential_search(my_list, -1, list_size)
        print binary_search_iterative(my_list, -1, list_size)
        print binary_search_recursive(my_list, -1, list_size)

        my_list = []
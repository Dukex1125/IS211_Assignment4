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


def insertion_sort(my_list, list_size):
    """Sorts the list with randomly generated values.

    Args:
        my_list (list): empty list to be filled with random integers
        list_size (int): value to determine size of list
    Returns:
        my_list (list): list of sorted values with size determined by list_size value
        str: string of time required to perform the sort.
    Example:
        >>>insertion_sort(my_list, 5)
    ([0, 0, 0, 1, 4], 'Insertion sort requires  0.0000062 seconds to perform.')
    """

    random_list(my_list, list_size)

    start = time.time()

    for index in range(1, len(my_list)):
        current_value = my_list[index]
        position = index

        while position > 0 and my_list[position - 1] > current_value:
            my_list[position] = my_list[position - 1]
            position = position -1

        my_list[position] = current_value
    end = time.time()

    return my_list, "Insertion sort requires %10.7f seconds to run, on average." % (end - start)


def shell_sort(my_list, list_size):
    """Sorts the list with randomly generated values.

    Args:
        my_list (list): empty list to be filled with random integers
        list_size (int): value to determine size of list
    Returns:
        my_list (list): list of sorted values with size determined by list_size value
        str: string of time required to perform the sort.
    Example:
        >>>shell_sort(my_list, 5)
        [0, 0, 3, 3, 5] Shell Sort requires  0.0000119 seconds to run, on average.
    """


    random_list(my_list, list_size)

    start = time.time()
    sublist_count = len(my_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(my_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end = time.time()

    return my_list, 'Shell Sort requires %10.7f seconds to run, on average.' % (end - start)


def gap_insertion_sort(my_list, start, gap):

    for i in range(start + gap, len(my_list), gap):
        current_value = my_list[i]
        position = i

        while position >= gap and my_list[position - gap] > current_value:
            my_list[position] = my_list[position - gap]
            position = position - gap

        my_list[position] = current_value


if __name__ == '__main__':
    for i in range(100):
        for list_size in (500, 1000, 10000):
            print insertion_sort(my_list, list_size)
            print shell_sort(my_list, list_size)
            my_list = []

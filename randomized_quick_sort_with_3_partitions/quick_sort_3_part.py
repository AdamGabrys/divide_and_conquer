# Randomized quick sort with 3 partitions (very efficient even for sequences of many equal elements)
# Input:
#   Length of array
#   Elements in array
# Output:
#    Sorted array
# ie.
#   5
#   2 3 9 2 2
#   Output: 2 2 2 3 9


import sys
import random


def main():
    inp = sys.stdin.read()
    array2sort = list(map(int, inp.split()))
    n = array2sort[0]
    array2sort = array2sort[1:n+1]
    random_quick_sort_3_part(array2sort, 0, n-1)
    for element in array2sort:
        print(element, end=' ')


def random_quick_sort_3_part(array2sort, left_boundary, right_boundary):
    if left_boundary >= right_boundary:
        return
    higher_beginning_index, random_element, smaller_beginning_index, smaller_ending_index =\
        initialize_quick_sort(array2sort, left_boundary, right_boundary)
    higher_beginning_index, smaller_beginning_index, smaller_ending_index =\
        separate_smaller_and_larger_elements(array2sort, higher_beginning_index, left_boundary, random_element,
                                             right_boundary, smaller_beginning_index,smaller_ending_index)
    do_recursive_calls(array2sort, higher_beginning_index, left_boundary, right_boundary, smaller_beginning_index,
                       smaller_ending_index)
    return array2sort


def separate_smaller_and_larger_elements(array2sort, higher_beginning_index, left_boundary, random_element,
                                         right_boundary, smaller_beginning_index, smaller_ending_index):
    for index in range(left_boundary + 1, right_boundary + 1):
        higher_beginning_index, smaller_beginning_index, smaller_ending_index =\
            compare_elements_and_swap(array2sort, higher_beginning_index, index,
                                      random_element, smaller_beginning_index, smaller_ending_index)
    swap_all_equal_elements_to_final_position(array2sort, left_boundary, smaller_beginning_index, smaller_ending_index)
    return higher_beginning_index, smaller_beginning_index, smaller_ending_index


def compare_elements_and_swap(array2sort, higher_beginning_index, index, random_element, smaller_beginning_index,
                              smaller_ending_index):
    if array2sort[index] == random_element:
        swap_equal_elements(array2sort, higher_beginning_index, index, smaller_beginning_index)
        smaller_beginning_index += 1
        smaller_ending_index += 1
        higher_beginning_index += 1
    elif array2sort[index] < random_element:
        swap(array2sort, index, higher_beginning_index)
        smaller_ending_index += 1
        higher_beginning_index += 1
    return higher_beginning_index, smaller_beginning_index, smaller_ending_index


def swap_equal_elements(array2sort, higher_beginning_index, index, smaller_beginning_index):
    swap(array2sort, index, smaller_beginning_index)
    if higher_beginning_index != smaller_beginning_index:
        swap(array2sort, index, higher_beginning_index)


def swap_all_equal_elements_to_final_position(array2sort, left_boundary, smaller_beginning_index, smaller_ending_index):
    swap(array2sort, slice(smaller_beginning_index, smaller_ending_index + 1),
         slice(left_boundary, smaller_beginning_index))


def do_recursive_calls(array2sort, higher_beginning_index, left_boundary, right_boundary, smaller_beginning_index,
                       smaller_ending_index):
    random_quick_sort_3_part(array2sort, left_boundary, left_boundary + smaller_ending_index - smaller_beginning_index)
    random_quick_sort_3_part(array2sort, higher_beginning_index, right_boundary)


def initialize_quick_sort(array2sort, left_boundary, right_boundary):
    random_element, random_element_index = get_random_element(array2sort, left_boundary, right_boundary)
    swap(array2sort, left_boundary, random_element_index)
    smaller_beginning_index, smaller_ending_index, higher_beginning_index = initialize__begin_end_indexes(left_boundary)
    return higher_beginning_index, random_element, smaller_beginning_index, smaller_ending_index


def get_random_element(array, left_boundary, right_boundary):
    random_element_index = random.randint(left_boundary, right_boundary)
    random_element = array[random_element_index]
    return random_element, random_element_index


def swap(array, left_index, right_index):
    array[left_index], array[right_index] = array[right_index], array[left_index]


def initialize__begin_end_indexes(left_boundary):
    smaller_beginning_index = left_boundary + 1
    smaller_ending_index = left_boundary
    higher_beginning_index = left_boundary + 1
    return smaller_beginning_index, smaller_ending_index, higher_beginning_index

if __name__ == '__main__':
    main()

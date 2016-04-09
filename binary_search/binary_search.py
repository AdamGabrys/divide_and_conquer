# Uses python3
# Binary search
# Input:
#   First line contains positive int representing length of array to be searched and array of positive values
#   Second line contains positive int representing number of sought elements and elements to be searched
# Output:
#   Indexes of sought elements -1 represents that there is no occurance of such element in array
# ie.
# 5 1 5 8 12 13
# 5 8 1 23 1 11
# Output: 2 0 -1 0 -1


import sys


def main():
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n = data[0]
    m = data[n + 1]
    list_to_be_searched = data[1 : n + 1]
    b = data[n + 2:]
    for sought_element in b:
        print(binary_search(0, n-1, list_to_be_searched, sought_element), end=' ')


def binary_search(left_boundary, right_boundary, list_to_be_searched, sought_element):
    middle_index = (right_boundary + left_boundary)//2
    middle_element = list_to_be_searched[middle_index]
    if sought_element == middle_element:
        return middle_index
    if left_boundary == right_boundary:
        return -1
    if sought_element > middle_element:
        return binary_search(middle_index+1, right_boundary, list_to_be_searched, sought_element)
    if sought_element < middle_element:
        return binary_search(left_boundary, middle_index, list_to_be_searched, sought_element)


if __name__ == '__main__':
    main()

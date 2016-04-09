# Uses python3
# Counts number o inversions for a sequence // based on merge sort modification
# Input:
#   sequence length
#   sequence elements
# Output:
#   number of inversions
# ie.
#   5
#   2 3 9 2 9
# Output: 2
# exp: (1, 3) (a1 = 3 > 2 = a3) and (2, 3) (a2 = 9 > 2 = a3).


import sys


def main():
    input_data = sys.stdin.read()
    list_length, *main_list = list(map(int, input_data.split()))
    merge_help_list = list_length * [0]
    print(get_number_of_inversions(main_list, merge_help_list, 0, list_length))


def get_number_of_inversions(main_list, merge_help_list, left_boundary_iterator, right_boundary_iterator):
    number_of_inversions = 0
    if right_boundary_iterator - left_boundary_iterator <= 1:
        return number_of_inversions
    middle_iterator = (left_boundary_iterator + right_boundary_iterator) // 2
    number_of_inversions += get_number_of_inversions(main_list, merge_help_list,
                                                     left_boundary_iterator, middle_iterator)
    number_of_inversions += get_number_of_inversions(main_list, merge_help_list, middle_iterator,
                                                     right_boundary_iterator)
    number_of_inversions += merge(main_list, merge_help_list, left_boundary_iterator,
                                  middle_iterator, right_boundary_iterator)
    return number_of_inversions


def merge(main_list, merge_help_list, left_boundary_iterator, middle_iterator, right_boundary_iterator):
    number_of_inversions = 0
    left_side_array_iter = left_boundary_iterator
    right_side_array_iter = middle_iterator
    i = left_side_array_iter
    while left_side_array_iter < middle_iterator and right_side_array_iter < right_boundary_iterator:
        if main_list[left_side_array_iter] > main_list[right_side_array_iter]:
            merge_help_list[i] = main_list[right_side_array_iter]
            right_side_array_iter += 1
            number_of_inversions += middle_iterator - left_side_array_iter
        else:
            merge_help_list[i] = main_list[left_side_array_iter]
            left_side_array_iter += 1
        i += 1
    if left_side_array_iter == middle_iterator:
        merge_help_list[i:right_boundary_iterator] = main_list[right_side_array_iter:right_boundary_iterator]
        main_list[left_boundary_iterator:right_boundary_iterator] =\
            merge_help_list[left_boundary_iterator:right_boundary_iterator]
    elif right_side_array_iter == right_boundary_iterator:
        merge_help_list[i:right_boundary_iterator] = main_list[left_side_array_iter:middle_iterator]
        main_list[left_boundary_iterator:right_boundary_iterator] =\
            merge_help_list[left_boundary_iterator:right_boundary_iterator]
    return number_of_inversions

if __name__ == '__main__':
    main()

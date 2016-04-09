# Uses python3
# Check whether an input sequence contains a majority element
# Input:
#   sequence length
#   sequence elements
# Output:
#   1 if there is major el or 0 if there is not
# ie.
#   5
#   2 3 9 2 9
# Output: 0


import sys


def get_majority_element(a, left, right):
    if left == right:
        return a[left]
    left_indexes = get_left_part_indexes(left, right)
    right_indexes = get_right_part_indexes(left, right)
    left_majority_element = get_majority_element(a, left_indexes[0], left_indexes[1])
    right_majority_element = get_majority_element(a, right_indexes[0], right_indexes[1])
    if left_majority_element == right_majority_element:
        return left_majority_element
    else:
        lme_count = count_num(a, left_majority_element, left, right)
        rme_count = count_num(a, right_majority_element, left, right)
        if lme_count > len(a[left:right+1])/2:
            return left_majority_element
        if rme_count > len(a[left:right+1])/2:
            return right_majority_element
    return -1


def count_num(a, el, l, r):
    count = 0
    for e in a[l:r+1]:
        if e == el:
            count += 1
    return count


def get_left_part_indexes(left, right):
    return left, (left+right)//2


def get_right_part_indexes(left, right):
    return (left+right)//2+1, right


if __name__ == '__main__':
    input_data = sys.stdin.read()
    n, *a = list(map(int, input_data.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)

# Uses python3
# The goal in this problem is given a set of segments on a line and a set of points on a line, to count, for each
# point, the number of segments which contain it.
# Solved using modified randomized quick sort which sort sequence of points, beginings and ends of segments.
# Sequences are combined to form of sequence ie. '3b''4b''5p''6e''7p''8e'
# Where b means beining of segemnt e end of segment p point. That allows then to solve problem with O(n+s)
# Quick sort kick it up so O((n+s)log(n+s)) is real big O
# input :
#   num_of_segments num_of_points
#   segment begin segment end
#   points
# ie:
#   3 2
#   0 5
#   -3 2
#   7 10
#   1 6
# Output: 2 0


def main():
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n = data[0]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    indicts = ['l'] * len(starts) + ['r'] * len(ends) + ['p'] * len(points)
    contanctates = starts + ends + points
    random_quick_sort_3_part(contanctates, 0, len(contanctates)-1, indicts)
    points_indices = list(range(0, len(points)))
    random_quick_sort_3_part(points, 0, len(points)-1, points_indices)
    deepnes = 0
    point_index = 0
    for i in range(0, len(contanctates)):
        if indicts[i] == 'l':
            deepnes += 1
        elif indicts[i] == 'r':
            deepnes -= 1
        elif indicts[i] == 'p':
            cnt[points_indices[point_index]] = deepnes
            #cnt[point_index] = deepnes
            point_index += 1
    return cnt


def random_quick_sort_3_part(array2sort, left_boundary, right_boundary, binded_array):
    if left_boundary >= right_boundary:
        return
    higher_beginning_index, random_element, smaller_beginning_index, smaller_ending_index =\
        initialize_quick_sort(array2sort, left_boundary, right_boundary, binded_array)
    higher_beginning_index, smaller_beginning_index, smaller_ending_index =\
        separate_smaller_and_larger_elements(array2sort, higher_beginning_index, left_boundary, random_element,
                                             right_boundary, smaller_beginning_index,smaller_ending_index, binded_array)
    do_recursive_calls(array2sort, higher_beginning_index, left_boundary, right_boundary, smaller_beginning_index,
                       smaller_ending_index, binded_array)
    return array2sort


def separate_smaller_and_larger_elements(array2sort, higher_beginning_index, left_boundary, random_element,
                                         right_boundary, smaller_beginning_index, smaller_ending_index, binded_array):
    for index in range(left_boundary + 1, right_boundary + 1):
        higher_beginning_index, smaller_beginning_index, smaller_ending_index =\
            compare_elements_and_swap(array2sort, higher_beginning_index, index,
                                      random_element, smaller_beginning_index, smaller_ending_index, binded_array)
    swap_all_equal_elements_to_final_position(array2sort, left_boundary, smaller_beginning_index, smaller_ending_index,
                                              binded_array)
    return higher_beginning_index, smaller_beginning_index, smaller_ending_index


def compare_elements_and_swap(array2sort, higher_beginning_index, index, random_element, smaller_beginning_index,
                              smaller_ending_index, binded_array):
    if array2sort[index] == random_element:
        swap_equal_elements(array2sort, higher_beginning_index, index, smaller_beginning_index, binded_array)
        smaller_beginning_index += 1
        smaller_ending_index += 1
        higher_beginning_index += 1
    elif array2sort[index] < random_element:
        swap(array2sort, index, higher_beginning_index)
        swap(binded_array, index, higher_beginning_index)
        smaller_ending_index += 1
        higher_beginning_index += 1
    return higher_beginning_index, smaller_beginning_index, smaller_ending_index


def swap_equal_elements(array2sort, higher_beginning_index, index, smaller_beginning_index, binded_array):
    swap(array2sort, index, smaller_beginning_index)
    swap(binded_array, index, smaller_beginning_index)
    if higher_beginning_index != smaller_beginning_index:
        swap(array2sort, index, higher_beginning_index)
        swap(binded_array, index, higher_beginning_index)


def swap_all_equal_elements_to_final_position(array2sort, left_boundary, smaller_beginning_index, smaller_ending_index,
                                              binded_array):
    if type(binded_array[left_boundary]) == str:
        l = 0
        r = 0
        p = 0
        for i in range(left_boundary, smaller_beginning_index):
            if binded_array[i] == 'l':
                l += 1
            elif binded_array[i] == 'r':
                r += 1
            elif binded_array[i] == 'p':
                p += 1
        binded_array[left_boundary:l+left_boundary] = ['l']*l
        binded_array[smaller_beginning_index-r:smaller_beginning_index] = ['r']*r
        binded_array[left_boundary+l:left_boundary+l+p] = ['p']*p
    swap(array2sort, slice(smaller_beginning_index, smaller_ending_index + 1),
         slice(left_boundary, smaller_beginning_index))
    swap(binded_array, slice(smaller_beginning_index, smaller_ending_index + 1),
         slice(left_boundary, smaller_beginning_index))


def do_recursive_calls(array2sort, higher_beginning_index, left_boundary, right_boundary, smaller_beginning_index,
                       smaller_ending_index, binded_array):
    random_quick_sort_3_part(array2sort, left_boundary, left_boundary + smaller_ending_index - smaller_beginning_index,
                             binded_array)
    random_quick_sort_3_part(array2sort, higher_beginning_index, right_boundary, binded_array)


def initialize_quick_sort(array2sort, left_boundary, right_boundary, binded_array):
    random_element, random_element_index = get_random_element(array2sort, left_boundary, right_boundary)
    swap(array2sort, left_boundary, random_element_index)
    swap(binded_array, left_boundary, random_element_index)
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

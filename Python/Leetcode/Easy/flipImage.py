
def flipImage(nested_array):
    flipped_list = [lists[::-1] for lists in nested_array]

    for number in range(len(flipped_list)):
        index_of_flipped_list = len(flipped_list) - 1
        while index_of_flipped_list >= 0:
            if flipped_list[number][index_of_flipped_list] == 0:
                flipped_list[number][index_of_flipped_list] = 1
                index_of_flipped_list -= 1
            else:
                flipped_list[number][index_of_flipped_list] = 0
                index_of_flipped_list -= 1
    return flipped_list


print(flipImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))

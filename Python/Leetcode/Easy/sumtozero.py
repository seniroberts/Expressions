def sumZero(integer):
    build_list = list(range(1, integer))
    sum_list = sum(build_list)
    build_list.append(-sum_list)
    return build_list


print(sumZero(3))

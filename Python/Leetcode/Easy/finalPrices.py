def finalPrices(price_array):

    for i in range(len(price_array)):
        for j in range(i + 1, len(price_array)):
            if price_array[j] <= price_array[i]:
                price_array[i] = price_array[i] - price_array[j]
                break
    return price_array


def test():
    price_array1 = [8, 4, 6, 2, 3]
    print(price_array1, "dicount:-->", finalPrices(price_array1))


test()


# def finalPrices2(price_array):
#     result = []
#     for i in range(len(price_array)):
#         seen = 0

#         for j in range(i + 1, len(price_array)):
#             if not seen and price_array[i] >= price_array[j]:
#                 result.append(price_array[i] - price_array[j])
#                 seen = 1

#         if not seen:
#             result.append([price_array[i]])
#     return [x for y in result for y in x]


# def test():
#     price_array1 = [8, 4, 6, 2, 3]
#     print(price_array1, "dicount2:-->", finalPrices2(price_array1))


# test()

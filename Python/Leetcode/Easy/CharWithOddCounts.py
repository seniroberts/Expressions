def CharWithOddCount(number):
    result = ""
    if number % 2 == 0:
        result += "a" * (number - 1) + "b"
    else:
        result += "a" * number
    return result


def test():
    number = 7
    print(number, "Odd Characters--->", CharWithOddCount(number))


test()

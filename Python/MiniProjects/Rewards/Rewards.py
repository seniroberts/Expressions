
# A function to extract contents from a txt file into an array
def readTextFile(fileName):
    an_array = []
    with open(fileName, "r") as the_file:
        the_file = the_file.readlines()

    for value in the_file:
        an_array.append(value.rstrip("\r\n"))
    return an_array

# Main program starts here


def getRewardList():
    names = readTextFile("rewards.txt")
    return names


def rewardManager(value):
    student_list = getRewardList()
    count = 0

    for name in student_list:
        if name == value:
            count += 1
    return count


def test():
    search_item = "Alexis"
    search_count = rewardManager(search_item)
    print("{} appears {} times".format(search_item, search_count))


test()


def readTextFile2(filename):
    list = []
    file = open(filename, "r")
    for value in file:
        # strip out all tailing whitespace and carriage returns
        list.append(value.rstrip('\r\n'))
    file.close()
    return list


# Main Program Starts Here
pupils = readTextFile2("rewards.txt")
# print(pupils)

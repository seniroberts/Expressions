import random

card_deck = ["a", "b", "c", "d", "e", "f"]


def shuffleCards(card_deck):
    numberofCards = len(card_deck)

    for i in range(0, numberofCards - 1):
        randon_number = random.randint(0, numberofCards-1)
        temp = card_deck[i]
        card_deck[i] = card_deck[randon_number]
        card_deck[randon_number] = temp
    return card_deck   # To return the shuffled list

    # use the below to return individual cards
    for i in range(0, numberofCards):
        print(card_deck[i])


# print(shuffleCards(card_deck))


nums = [10, 2, 13, 4, 51, 6, 17]


def sortList(nums):
    for i in range(0, len(nums)):
        for j in range(i + 1, (len(nums))):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums


print(sortList(nums))

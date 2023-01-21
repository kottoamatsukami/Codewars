"""
DESCRIPTION:
Write a function that takes an array of numbers (integers for the tests) and a target number.
It should find two different items in the array that,
when added together, give the target value.
The indices of these items should then be returned in a tuple / list (depending on your language)
like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all the items will be numbers;
target will always be the sum of two different items from that array).
"""


def two_sum(lst: list, target) -> list:
    for ind_1 in range(len(lst)):
        for ind_2 in range(ind_1+1, len(lst)):
            if lst[ind_1]+lst[ind_2] == target:
                return [ind_1, ind_2]

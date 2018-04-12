""" CLI program to test HW3 homework """
# Tianyi Yang
import argparse
from HW3 import words_containing, len_safe, unique


def test_words_containing():
    # Test 1
    # If test1 passed, head to test2
    # If test1 failed, return False immidiately
    sentenses = """The people who get on in this world are the people who get
                up and look for circumstances they want,
                and if they cannot find them, make them.——Bernara Shaw"""
    letter = 'o'
    list1 = words_containing(sentenses, letter)
    list2 = ["people", "who", "on", "world", "people", "who", "look", "for",
             "cannot"]
    i = 0
    while (i < len(list1)):
        if list1[i] == list2[i]:
            i = i + 1
            continue
        else:
            return False
    if (len(list1) == len(list2)):
        test1 = True
    else:
        return False
    # Test2 empty list
    sentenses = ""
    letter = 'a'
    list1 = words_containing(sentenses, letter)
    list2 = []
    if list1 == list2:
        test2 = True
    else:
        return False
    if test1 is True and test2 is True:
        return True

    """Return True/False if the test of words_containing passes/fails"""


def test_len_safe():
    # Test1
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    if len_safe(list1) != 8:
        return False

    # Test2
    dic1 = {'1': 23, '2': 45, '3': 89, '4': "yoyo", '5': list1}
    if len_safe(dic1) != 5:
        return False

    # Test3
    if len_safe([]) != 0:
        return False

    # Test4
    if len_safe(8) != -1:
        return False
    else:
        return True

    """Return True/False if the test of len_safe passes/fails"""


def test_unique():
    i = 0
    numbers = [2, 6, 5, 7, 7, 3, 9, 3, 2, 8]
    nums = unique(numbers)
    list1 = [2, 6, 5, 7, 3, 9, 8]
    while (i < len(list1)):
        if next(nums) == list1[i]:
            i = i+1
            continue
        else:
            return False
    try:
        next(nums)
    except StopIteration:
        return True
    else:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--unique', help="""Flag to test the unique
                        function from HW3""", action="store_true")
    parser.add_argument('-w', '--works', help="""Flag to test the
                    words_containing function from HW3""", action="store_true")
    parser.add_argument('-l', '--len', help="""Flag to test the len_safe
                        function from HW3""", action="store_true")
    arguments = parser.parse_args()
    if arguments.unique:
        if test_unique() is True:
            print("unique passed")
        else:
            print("unique failed")

    if arguments.works:
        if test_words_containing()is True:
            print("words_containing passed")
        else:
            print("words_containing failed")

    if arguments.len:
        if test_len_safe() is True:
            print("len_safe passed")
        else:
            print("len_safe failed")

    # Set up argparse information here

    # Based on user input, run test(s) requested and print outcome

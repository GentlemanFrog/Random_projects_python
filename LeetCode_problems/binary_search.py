# Divide and conquer algorithm

# We trying to prove that binary search is faster then naive search
# Naive search scan entire list and usk if its equal to the target

import random
import time


def naive_search(random_list, target):
    for i in range(len(random_list)):
        if random_list[i] == target:
            return i
    return -1


def binary_search(random_list, target, low=None, high=None):

    # We taking advantege from fact that list is sorted
    # Our aim is to split the whole list in half and then check if we have to look
    # for our target number in whole list or we just need to check the left side or right and split
    # it more... and split and...
    # The low and high parameters give us information on what is the highest and the lowes indcies
    # on the list in the next recursion

    if high >= low:

        midpoint = (high + low) // 2

        if random_list[midpoint] == target:
            return midpoint
        elif random_list[midpoint] > target:
            return binary_search(random_list, target, low, midpoint-1)
        else:
            # target > random_list[midpoint] so we have to do another binary search
            return binary_search(random_list, target, midpoint+1, high)
    else:
        # Element not represented in list
        return -1


if __name__ == '__main__':

    #target = 6
    #print(f'Target number we are looking for: {target}')

    # Generating random lists from range my approach
    # rand_list_for_search = random.sample(range(1, 30), 20)
    # rand_list_for_search.sort()
    # print(rand_list_for_search)

    # Internet approach:
    length = 10000
    # Building sorted list of length 10 000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    # Starting timer
    start = time.time()
    # Iterating through whole list (making all number target and search it)
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()

    # Output of time naive search need:
    print(f'Naive search working time per iterations: {(end - start)/length} s ')

    # Starting timer
    start = time.time()
    # Iterating through whole list (making all number target and search it)
    for target in sorted_list:
        binary_search(sorted_list, target, 0, len(sorted_list)-1)
    end = time.time()

    # Output of time naive search need:
    print(f'Binary search working time per iterations: {(end - start) / length} s ')

    # Writing the results of search: for testing purpose
    # if result_naive != -1:
    #    print(f'Element is presented at index: {result_naive}')
    # else:
    #    print('Element is not present in list. ')

    # if result_binary != -1:
    #    print(f'Element is presented at index: {result_binary}')
    # else:
    #    print("Element is not present in list. ")

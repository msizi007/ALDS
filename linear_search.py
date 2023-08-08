"""Time module for measuring time"""
import time


# This is an algorithm which searches a target number from list of numbers using linear search
# In linear search, the list doesn't have to be sorted
# We loop through list of numbers provided and search for target in each iteration
# if target is not found return false
# if target is found we return true

# critical cases to consider
# what if the list is empty ?

NUMBER_OF_TRIALS = 0

def Linear_Search(data_list: list, target: int):
    global NUMBER_OF_TRIALS

    # if list is empty then return False (target cannot exist at all)
    if len(data_list) == 0: # simplified =>  if data_list:
        return False
                     
    for num in data_list:
        # if target is found return true
        if num == target:
            return True
        NUMBER_OF_TRIALS += 1
    # if target wasn't found return false
    return False


def space_time_measure():
    start_time = time.time()
    Linear_Search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to complete: {elapsed_time} seconds!")
    print(f"Number of trials: {NUMBER_OF_TRIALS} trials..")

    
space_time_measure()

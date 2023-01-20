# https://practice.geeksforgeeks.org/problems/zero-sum-subarrays1825/1?page=1&difficulty[]=1&curated[]=1&sortBy=submissions
# sum = 0
# counter = 0
# iterate over items.
    # if item == 0 :
        # counter += 1
    # sum += item
    # if sum found in dict
        # counter += value from dict
    # append sum do dict counter


def f(arr):
    d = {0:1}
    sum_ = 0
    counter = 0
    for item in arr:
        sum_ += item
        if sum_ in d:
            counter += d[sum_]
            d[sum_] += 1
        else:
            d[sum_] = 1
    return counter

def log(v):
    print(v)
    return v

assert log(f([0,0,5,5,0,0])) == 6
assert log(f([0,0,0])) == 6
assert log(f([6,-1,-3,4,-2,2,4,6,-12,-7])) == 4

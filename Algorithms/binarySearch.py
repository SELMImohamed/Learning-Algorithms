def binary_search(list, items):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high)
        guess = list [mid]
        if guess == items:
            return mid
        if guess > items: 
            high = mid -1
        else:
            low = mid +1
    return None


my_list = [1, 3, 4, 5, 9]

print(binary_search(my_list, 10))
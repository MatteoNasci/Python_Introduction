def k_max(my_list, k):
    # copy_list = my_list[:]
    # copy_list.sort(reverse=True)
    # return copy_list[:k]
    return sorted(my_list, reverse=True)[:k]


def binary_sort(my_list, value):
    start = 0
    end = len(my_list) - 1
    while end >= start:
        index = (start + end)//2
        list_value = my_list[index]
        if(list_value == value):
            return True
        elif list_value > value:
            end = index - 1
        else:
            start = index + 1
    return False


def binary_sort_recursive(my_list, value, start, end):
    if end < start:
        return False
    middle = (end + start)//2
    list_value = my_list[middle]
    if list_value == value:
        return True
    elif list_value > value:
        return binary_sort_recursive(my_list, value, start, middle-1)
    else:
        return binary_sort_recursive(my_list, value, middle + 1, end)

def binary_sort_inverse(my_list, value):
    start = 0
    end = len(my_list) - 1
    while end >= start:
        index = (start + end)//2
        list_value = my_list[index]
        if(list_value == value):
            return True
        elif list_value < value:
            end = index - 1
        else:
            start = index + 1
    return False

def binary_sort_recursive_inverse(my_list, value, start, end):
    if end < start:
        return False
    middle = (end + start)//2
    list_value = my_list[middle]
    if list_value == value:
        return True
    elif list_value < value:
        return binary_sort_recursive(my_list, value, start, middle-1)
    else:
        return binary_sort_recursive(my_list, value, middle + 1, end)

def get_odds(max_value):
    numbers = list(range(max_value))
    return [number for number in numbers if number % 2] #!= 0 sottinteso, 0 è false, 1 è true

def get_odds_squared(max_value):
    numbers = list(range(max_value))
    return [number ** 2 for number in numbers if number % 2] #!= 0 sottinteso, 0 è false, 1 è true

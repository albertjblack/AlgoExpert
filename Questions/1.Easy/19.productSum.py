def productSum(arr, mult=1):
    my_sum = 0

    for element in arr:
        if type(element) is int:
            my_sum += element
        else:
            my_sum += productSum(element, mult + 1)
    return my_sum * mult

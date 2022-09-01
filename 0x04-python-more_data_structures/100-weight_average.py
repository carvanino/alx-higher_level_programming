#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    multiples = 0
    if not my_list:
        return 0
    for element in my_list:
        sum = sum + element[1]
        multiples = multiples + (element[0] * element[1])
        weightd_avg = multiples / sum
    return float(weightd_avg)

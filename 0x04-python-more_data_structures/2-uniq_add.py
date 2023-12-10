#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqe_set = set()
    result = 0
    for i in my_list:
        if i not in uniqe_set:
            result += i
            uniqe_set.add(i)
    return result

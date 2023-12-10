#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            replace_list.append(replace)
        else:
            replace_list.append(my_list[i])
    return replace_list

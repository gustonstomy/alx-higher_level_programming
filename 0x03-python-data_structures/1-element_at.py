#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list) - 1
    if idx > list_len:
        return None
    elif idx < 0:
        return None
    else:
        return my_list[idx]

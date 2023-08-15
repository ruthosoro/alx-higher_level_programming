#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    lastIndex = len(my_list) - 1
    if idx > lastIndex:
        return None
    return my_list[idx]

#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return None
    else:
        index = my_list[idx:idx+1]  # return (my-list[idx])
        for i in index:
            return(i)

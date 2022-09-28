#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = my_list[:]
    if not my_list:
        return None
    for item in my_list:
        if item == search:
            # Get the position of the item in the list
            pos = my_list.index(item)
            # Remove the item from its place
            my_list.remove(item)
            # Put the replacement in the removed item's position
            my_list.insert(pos, replace)
    return my_list

# Tests
_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(_list, 2, 89)

print(new_list)
print(_list)

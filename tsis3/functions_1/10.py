def unique(lst):
    new_list = []
    for x in lst:
        if x not in new_list:
            new_list.append(x)
    return new_list

print(unique([1, 1, 3, 5, 3, 6, 19]))


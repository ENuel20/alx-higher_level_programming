def element_at(my_list, idx):
    if idx < 0:
        return (None)

    length = len(my_list)

    if idx > length - 1:
        return (None)

    return("element of idx {} is {}".format(idx, my_list[idx]))

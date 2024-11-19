def remove_duplicates(a_list):

    newlist = []
    for item in a_list:
        if item not in newlist:
            newlist.append(item)
            

    return newlist

test = ["a", "b", "c", "c", "b", "c", "a", "a", "d"]
print(f"test list:{test}")
print(f"duplicates removed {remove_duplicates(test)}")
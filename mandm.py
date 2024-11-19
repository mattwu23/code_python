def mean (a_list):
    return sum(a_list) / len(a_list)

def median (a_list):

    m = len(a_list) // 2
    sorted_list = sorted(a_list)

    if m % 2 !=0:
        left = sorted_list[m-1]
        right = sorted_list[m]
        average =(left+right)/ 2
        return average
    else:
        return sorted_list[m]
def quicksort(a_list):
    if len(a_list) <= 1:
        return a_list
    pivot_pos = (len(a_list) -1)/2
    final_pivot_pos = partition(a_list,pivot_pos)
    a_list[0:final_pivot_pos] = quicksort(a_list[0:final_pivot_pos])
    a_list[final_pivot_pos+1:] = quicksort(a_list[final_pivot_pos+1:])
    return a_list

def partition(a_list, pivot_pos):
    pivot_val= a_list[pivot_pos]
    index = 0
    while index < len(a_list):
        value = a_list[index]
        if value < pivot_val:
            if index > pivot_pos:
                del a_list[index]
                a_list.insert(0, value)
                pivot_pos += 1
        elif value > pivot_val:
            if index < pivot_pos:
                del a_list[index]
                a_list.append(value)
                pivot_pos -= 1
                continue
        index += 1
    return pivot_pos


test_list = [1,100,30,5,3,2,4,4,7,1,23,40,10,9]
print test_list
quicksort(test_list)
print test_list

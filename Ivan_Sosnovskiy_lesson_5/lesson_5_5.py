src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#  result = [23, 1, 3, 10, 4, 11]

def get_new_list(our_list):
    result = []
    for item in our_list:
        if src.count(item) == 1:
            result.append(item)
    return result


results = get_new_list(src)
print(results)


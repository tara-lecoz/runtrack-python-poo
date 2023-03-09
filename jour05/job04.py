def listMax(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], listMax(list[1:]))
    
list = [5,48,3,84,8,56,47,78]
print(listMax(list))
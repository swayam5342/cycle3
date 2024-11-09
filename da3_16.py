def min_max(l:list)-> tuple[int, int]:
    return (max(l),min(l))
l: list[int]=[1,4,6,4,2,7,8,9,0]
print(min_max(l))
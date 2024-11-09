from typing import Any

def count(l:list)->None:
    count:dict[Any,Any]={}
    for i in l:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    print(count)

l: list[int]=[1,2,3,4,3,2,1,1,1,2,5,6,7,9,7,6,5]

count(l)
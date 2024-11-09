from typing import Any

def remove_dup(l:list)->list[str]:
    return list(dict.fromkeys(l))

li: list[Any]=[1,2,3,3]
li=remove_dup(li)
print(li)
from typing import Callable, Literal



calculator:Callable[[float,float,str],float | Literal['Undefined']] = lambda x, y, op: (
    x + y if op == "+" else
    x - y if op == "-" else
    x * y if op == "*" else
    x / y if op == "/" and y != 0 else
    "Undefined"
)
print(calculator(10, 5, "+"))  
print(calculator(10, 5, "*"))
print(calculator(10, 0, "/"))



orders_list1: list[str] = ["order1", "order2", "order3", "order5"]
orders_list2: list[str] = ["order2", "order3", "order4"]


orders_set1 = set(orders_list1)
orders_set2 = set(orders_list2)

unique_orders: set[str] = orders_set1.union(orders_set2)
print("Unique orders:", unique_orders)

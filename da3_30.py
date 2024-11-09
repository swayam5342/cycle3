
branch_A_customers: list[str] = ["cust1", "cust2", "cust3"]
branch_B_customers: list[str] = ["cust2", "cust4", "cust5"]

unique_customers: set[str] = set(branch_A_customers).union(set(branch_B_customers))
print("Unique customers:", unique_customers)

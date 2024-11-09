
subscribers_A: set[str] = {"Alice", "Bob", "Charlie"}
subscribers_B: set[str] = {"Charlie", "David", "Emma"}


all_subscribers: set[str] = subscribers_A | subscribers_B
print("Union:", all_subscribers)


common_subscribers: set[str] = subscribers_A & subscribers_B
print("Intersection:", common_subscribers)


diff_A_B: set[str] = subscribers_A - subscribers_B
print("Difference A - B:", diff_A_B)


symmetric_diff: set[str] = subscribers_A ^ subscribers_B
print("Symmetric Difference:", symmetric_diff)

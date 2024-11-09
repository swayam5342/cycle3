
participants: list[tuple[str, float]] = [("Alice", 5.6), ("Bob", 5.9), ("Charlie", 5.7)]
participants_sorted: list[tuple[str, float]] = sorted(participants, key=lambda x: x[1], reverse=True)
print("Participants sorted by height (descending):")
for participant, height in participants_sorted:
    print(f"{participant}: {height}")

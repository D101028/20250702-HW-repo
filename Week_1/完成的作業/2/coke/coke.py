remains = 50
while remains > 0:
    print(f"Amount Due: {remains}")
    inserted = int(input("Insert Coin: "))
    remains -= inserted
print(f"Change Owed: {-remains}")

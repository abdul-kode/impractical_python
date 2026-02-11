"""Input cipher key string, get user input on route direction as dict value."""

col_order = """1 3 4 2"""
key = dict()
cols = [int(i) for i in col_order.split()]
for col in cols:
    while True:
        key[col] = input(f"Direction to read Column {str(col).lower()} (u = up, d = down): ")
        if key[col] == 'u' or key[col] == 'd':
            break
        else:
            print("Input should be 'u' or 'd'")

    print(f"{col}, {key[col]}")

print(f"\nFinal key dictionary: {key}")

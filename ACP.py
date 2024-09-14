total = int(input("Enter total amount:"))

notes = [
    5000,
    1000,
    500,
    100,
    50,
    20,
    10,
    5
]

print(f"To split {total} across notes you will get:")

for i in notes: 
    n = total // i
    total %= i
    if n != 0: print(f"  - {n} note(s) worth {i}.")
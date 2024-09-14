def combs(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    st2 = 0
    st1 = 0

    if (n >= 2):
        print(f"\x1b[33mIteration completed: {n} and {n-2}\x1b[0m")
        st2 = combs(n-2)
    st1 = combs(n-1)

    return st1+st2

stairs = int(input("stair n? "))
print("Number of ways to use one step and two steps:", combs(stairs))
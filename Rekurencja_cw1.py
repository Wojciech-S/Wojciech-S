#Napisz funkcję liczącą silnię

def decrement(n):
    if n > 1:
        return n*decrement(n-1)
    elif n == 0:
        print(1)
        return
print(decrement()

assert decrement("silnia"(0)) == 1
assert decrement("silnia"(1)) == 1
assert decrement("silnia"(2)) == 2
assert decrement("silnia"(3)) == 6
assert decrement("silnia"(4)) == 24
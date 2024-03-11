x: int = 1
count: int = 0
z: int = 12


while x < z:
    count += 1
    if z % 2 == 0:
        z /= 2
    elif x == 1:
        x += 4
    else:
        x += 1

print(x)
print(count)
print(z)
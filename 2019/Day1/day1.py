import math

# part 1 
def fuel_requirements(x):
    return (math.floor(x / 3) - 2)


assert fuel_requirements(12) ==2
assert fuel_requirements(14) == 2
assert fuel_requirements(1969) == 654
assert fuel_requirements(100756)==33583

sum = 0
with open("input.txt", "r") as file:
    for line in file:
        mass = line.strip()
        sum += fuel_requirements(int(mass))
print(sum)
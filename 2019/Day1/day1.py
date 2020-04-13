import math

# part 1 
def fuel_requirements(x):
    return (math.floor(x / 3) - 2)

#part 1 tests
assert fuel_requirements(12) ==2
assert fuel_requirements(14) == 2
assert fuel_requirements(1969) == 654
assert fuel_requirements(100756)==33583



#part2 tests
# assert 14 == 2
# assert 1969 == 966
# assert 100756 == 50346 

sum = 0
with open("input.txt", "r") as file:
    for line in file:
        mass = line.strip()
        sum += fuel_requirements(int(mass))
print(sum)
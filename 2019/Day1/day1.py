# part 1 
def fuel_requirements(x):
    return (x // 3 - 2)

def mass(x):
    return x

#part 1 tests
assert fuel_requirements(12) ==2
assert fuel_requirements(14) == 2
assert fuel_requirements(1969) == 654
assert fuel_requirements(100756)==33583



#part2

def fuel_for_fuel(x):
    sum = 0
    while fuel_requirements(x) >= 0:
        x = fuel_requirements(x)
        sum += x
    return sum
#part2 tests

assert fuel_for_fuel(14) == 2
assert fuel_for_fuel(1969) == 966
assert fuel_for_fuel(100756) == 50346 

p1sum = 0
p2sum = 0
with open("input.txt", "r") as file:
    for line in file:
        mass = line.strip()
        p1sum += fuel_requirements(int(mass))
        p2sum += fuel_for_fuel(int(mass))
print(p2sum)
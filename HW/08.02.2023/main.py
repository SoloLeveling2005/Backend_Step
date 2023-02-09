mass = [1, 5, 8, 3, 1, 6, 8, 9, 3, 2, 54, 7]
# Первый способ

for i in mass:
    for j in mass:
        if i > j:

            mass[mass.index(i)], mass[mass.index(j)] = j, i
            print(mass)

print(mass)
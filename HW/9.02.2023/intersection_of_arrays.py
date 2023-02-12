mass_one = [1, 2, 3, 2, 0]
mass_two = [5, 1, 2, 7, 3, 2]


def find_data(mass1, mass2):
    mass_new = []

    if len(mass1) > len(mass2):
        for i in mass2:
            if i in mass1:
                mass_new.append(i)
                mass1.remove(i)
    else:
        for i in mass1:
            if i in mass2:
                mass_new.append(i)
                mass2.remove(i)
    return sorted(mass_new)


print(find_data(mass_one, mass_two))

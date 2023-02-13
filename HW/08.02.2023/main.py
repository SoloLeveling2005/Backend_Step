mass = [12, 5, 8, 3, 1, 6, 8, 9, 3, 2, 54, 7]


# Первый способ (пузырьком)

def sort1(array):
    change = False
    for index, value in enumerate(array):
        try:
            one = array[index]
            two = array[index + 1]
            if one > two:
                array[index], array[index + 1] = two, one
                change = True
        except:
            print("Массив закончился")
            print(array) if change else sort1(array)


sort1(mass)

# Второй способ (сортировка)
print("\n\n\n")


def sort2(array):
    new_array = []
    index = 0
    value = array[index]

    while True:

        # todo, find min value
        for i, v in enumerate(array):
            if value > v:
                index = i
                print(value)
                print(index)

        # print(array[index])
        new_array.append(array[index])

        # print(new_array)
        # todo, exit cycle
        if len(array) == len(new_array):
            break



sort2(mass)

def recursion(string):
    string = string.lower().replace(' ', '')
    if len(string) <= 1:
        print("Это палиндром, recursion")
        return True
    if string[0] == string[-1]:
        return recursion(string[1:-1])
    else:
        print("Это НЕ палиндром, recursion")
        return False


def reverse(string):
    string = string.lower().replace(' ', '')
    print("Это палиндром, reverse") if string == string[::-1] else print("Это НЕ палиндром, reverse")


def pointers(string):
    string = string.lower().replace(' ', '')
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            print("Это НЕ палиндром, pointers")
            return False
        left += 1
        right -= 1
    print("Это палиндром, pointers")
    return True


str_1 = "Казак"
str_2 = "А роза упала на лапу Азора"
str_3 = "Do geese god?"
str_4 = "Madam, I`m Adam"

print(str_1)
recursion(str_1)
reverse(str_1)
pointers(str_1)
print("-----------------------")

print(str_2)
recursion(str_2)
reverse(str_2)
pointers(str_2)
print("-----------------------")

print(str_3)
recursion(str_3)
reverse(str_3)
pointers(str_3)
print("-----------------------")

print(str_4)
recursion(str_4)
reverse(str_4)
pointers(str_4)
print("-----------------------")



# todo не получилось реализовать range_extraction поэтому поискал в интернете

mass_ = [6, 4, 3, 1, 8, 5, 9]

def range_extraction(lst):
    sorted_lst = sorted(lst)
    ranges = []
    start = end = sorted_lst[0]
    for num in sorted_lst[1:]:
        if num == end + 1:
            end = num
        else:
            ranges.append((start, end))
            start = end = num
    ranges.append((start, end))
    return ','.join(f'{r[0]}-{r[1]}' if r[0] != r[1] else str(r[0]) for r in ranges)

print(range_extraction(mass_))

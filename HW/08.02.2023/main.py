import random
import time

# Мои способы
# mass = [12, 5, 8, 3, 1, 6, 8, 9, 3, 2, 54, 7]


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


# sort1(mass)
# Второй способ (выборка)
print("\n\n\n")


def sort2(array):
    new_array = []

    while True:
        smallest_value = None
        for j in array:
            if smallest_value is None or smallest_value > j:
                smallest_value = j
        array.remove(smallest_value)
        new_array.append(smallest_value)
        if len(array) == 0:
            break
    print(new_array)


# sort2(mass)


# todo Тестирование существующих способов
def start_time(func):
    def wrapper(mass):
        start_timer = time.time()
        func(mass)
        end_timer = time.time()
        elapsed_time = end_timer - start_timer
        print(str(elapsed_time)[:7])
        return elapsed_time

    return wrapper


mass = [random.randint(0, 1000) for _ in range(1000)]
print(mass)


# todo Пузырьковая сортировка, время сортировки 0.14119
@start_time
def bubble_sort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True


bubble_sort(mass)
print(mass)


# todo Сортировка выборкой, время сортировки 0.03902
@start_time
def selection_sort(nums):
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


# Проверяем, что оно работает
# selection_sort(mass)
# print(mass)


# todo Сортировка вставками, время сортировки 0.04003
@start_time
def insertion_sort(nums):
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert


# Проверяем, что оно работает
# insertion_sort(mass)
# print(mass)


# todo Пирамидальная сортировка, время сортировки 0.00602
def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считаем корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — допустимый индекс, а элемент больше,
    # чем текущий наибольший, обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент больше не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


@start_time
def heap_sort(nums):
    n = len(nums)

    # Создаём Max Heap из списка
    # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


# Проверяем, что оно работает
# heap_sort(mass)
# print(mass)


# todo Сортировка слиянием, время сортировки 0.00500
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


# Проверяем, что оно работает
# start_timer = time.time()
# mass = merge_sort(mass)
# end_timer = time.time()
# elapsed_time = end_timer - start_timer
# print(elapsed_time)
# print(mass)


# todo Быстрая сортировка, время сортировки 0.00199
def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

# Проверяем, что оно работает
# start_timer = time.time()
# mass = merge_sort(mass)
# end_timer = time.time()
# elapsed_time = end_timer - start_timer
# print(elapsed_time)
# print(mass)



# todo in GO
# todo Сортировка пузырьком на GO заняло 0,000595 секунд

# package main
#
# import (
# 	"fmt"
# 	"math/rand"
# 	"time"
# )
#
# // BubbleSort todo Sort by bubble
# func BubbleSort(array []int) []int {
# 	for i := 0; i < len(array)-1; i++ {
# 		for j := 0; j < len(array)-i-1; j++ {
# 			if array[j] > array[j+1] {
# 				array[j], array[j+1] = array[j+1], array[j]
# 			}
# 		}
# 	}
# 	return array
# }
# func main() {
# 	start := time.Now()
# 	// Инициализируем генератор случайных чисел с использованием текущего времени
# 	rand.Seed(time.Now().Unix())
#
# 	// Задаем длину массива и создаем его
# 	length := 1000
# 	arr := make([]int, length)
#
# 	// Заполняем массив случайными числами
# 	for i := 0; i < length; i++ {
# 		arr[i] = rand.Intn(1000)
# 	}
#
# 	array := arr
# 	fmt.Println(BubbleSort(array))
# 	elapsed := time.Since(start)
# 	fmt.Printf("Время выполнения: %s\n", elapsed)
# }
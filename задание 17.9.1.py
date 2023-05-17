numbers = input("Введите последовательность чисел через пробел ").split()
element = int(input("Введите число "))
array = list(map(int, numbers))

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print("Отсортированный список")
print((array))
def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] < element and array[middle+1] >= element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

if element < array[0] or element > array[-1]:
    print("Число не соответствует условию")
else:
    print("Индекс элемента, соответствующего условию")
    print(binary_search(array, element, 0, len(array)))
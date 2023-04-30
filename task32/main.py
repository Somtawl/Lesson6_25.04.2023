from random import randint

array_size = int(input("Введите размер массива "))
min = int(input("Введите минимальный элемент "))
max = int(input("Введите максимальный элемент "))

def fill_array(size):
    array = []
    for i in range(array_size):
        array.append(randint(1,100))
    return array

def finde_index(array):
    result = []
    for i in range(array_size):
        if array[i] < max and array[i] > min:
            result.append(i)
    return result

array = fill_array(array_size)
print("Массив ",array)
print("Найденные элементы ",finde_index(array))
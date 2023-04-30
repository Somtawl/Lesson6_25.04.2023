first_element = int(input("Введите первый элемент "))
difference = int(input("Введите разность "))
total_elements = int(input("Введите общее число элементов "))
current_element = first_element
result = []

for i in range(total_elements):
    result.append(current_element)
    current_element = current_element + difference

print(result)
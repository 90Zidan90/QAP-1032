numbers_spisok = input("Введите последовательность целых чисел через пробел: ")
numbers_spisok_mod = [int(x) for x in numbers_spisok.split()]

try:
    user_number = int(input("Введите целое число: "))
    if user_number % 1 == 0:
        numbers_spisok_mod.append(user_number)
        print("Список до сортировки: ", numbers_spisok)
        numbers_spisok_mod.sort()
        print("Список после сортировки по возрастанию: ", numbers_spisok_mod)
    else:
        print("Введите число")
except ValueError:
    print("Не корректные данные,введите целое число")

def binary_search(numbers_spisok_mod, user, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if numbers_spisok_mod[middle] == user:
            return middle
        elif user < numbers_spisok_mod[middle]:
            return binary_search(numbers_spisok_mod, user, left, middle - 1)
        else:
            return binary_search(numbers_spisok_mod, user, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее числ'


print("Индекс введенного числа в списке: ", binary_search(numbers_spisok_mod, user_number, 0, len(numbers_spisok_mod) - 1))

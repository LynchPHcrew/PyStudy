#На вход программе подаются две строки текста, содержащие целые числа.
# Из данных строк формируются списки чисел L и M.
# Напишите программу, которая создает третий список, элементами которого являются суммы соответствующих элементов списков L и M.
# Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 пробел.
L = input().split()
M = input().split()
for i in range(len(L)):
    L[i] = int(L[i])
for j in range(len(M)):
    M[j] = int(M[j])
Itog = []
for i in range(len(L)):
    Itog.append(L[i] + M[i])
print(*Itog)
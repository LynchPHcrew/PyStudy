#На вход программе подается натуральное число n.
# Напишите программу, использующую списочное выражение, которая создает список содержащий квадраты чисел от 1 до n, а затем выводит его элементы построчно, то есть каждый на отдельной строке.
n = int(input())
set = [i ** 2 for i in range(1, n+1)]
print(*set, sep='\n')
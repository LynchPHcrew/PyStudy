# На вход программе подается натуральное число nn, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список,
# затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.
n = int(input())
list = []
for i in range(n):
    l = int(input())
    list.append(l)
del list[1::2]
print(list)
# На вход программе подается строка текста, содержащая различные натуральные числа.
# Из данной строки формируется список чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
s = input().split()
for i in range(0, len(s)):
    s[i] = int(s[i])
i = s.index(max(s))
j = s.index(min(s))
s[i], s[j] = s[j], s[i]
print(*s)
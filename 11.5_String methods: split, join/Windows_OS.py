# На вход программе подается одна строка с корректным именем файла в операционной системе Windows.
# Напишите программу, которая разбирает строку на части, разделенные символом "\". Каждую часть вывести в отдельной строке.
s = input()
razdelit = s.split('\\')
print(*razdelit, sep = '\n')
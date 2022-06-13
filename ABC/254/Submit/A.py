N = int(input())

second = N % 100 // 10
first = N % 100 % 10
print(second, first, sep='')

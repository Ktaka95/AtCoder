H, W = map(int, input().split())

first = False
first_location = [0] * 2
second_location = [0] * 2
for i in range (H):
    S = input()
    j = 0
    for s in S:
        if s == 'o':
            if first == False:
                first = True
                first_location[0] = i
                first_location[1] = j
            else:
                second_location[0] = i
                second_location[1] = j
        j += 1
x_diff = abs(first_location[0] - second_location[0])
y_diff = abs(first_location[1] - second_location[1])
print(x_diff + y_diff)

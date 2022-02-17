s = input()
t = input()

new_s = sorted(s)
new_t = sorted(t, reverse=True)

if new_s < new_t:
	print("Yes")
else:
	print("No")

n = int(input("Enter a value: "))

for i in range(n):
	if i != 0:
		for k in range(i):
			print("\\\\",end="")
	for l in range(n*4-2-4*i):
		print("!",end="")

	if i != 0:
		for m in range(i):
			print("//",end="")

	print()

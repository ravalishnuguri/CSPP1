x = int(input("enter the number: "))
sum = 0
for x in range(x,0,-1):
	sum += x
	x -= 1
print(sum)
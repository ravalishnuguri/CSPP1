# d = {1:"saad",2:"teja",3:"Ramu",4:"Gandhi",5:"Nehru"}
# z = {"s":"saad","t":"teja","r":"Ramu","g":"Gandhi","n":"Nehru"}
# print(z)
# # for i in z:
# # 	print(z[i])
# a = z.pop("s")
# print(a)
# # k = del(z["t"])

# print(z)

l = [1,2,3,4,5,6,7,[8,9,5],8,9]
# print(type(l))
su = 0
for i in l:
	if type(i) == list:
		su+=sum(i)
		print("True")

		# for j in range(len(l[i])):
		# 	su+=l[i][j]
	su+=l[i]
	print(su)
print(su)

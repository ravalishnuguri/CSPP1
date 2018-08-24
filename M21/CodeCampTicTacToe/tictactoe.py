
def valid(row):
	for i in row:
		len(i) != 3
		return "invalid game"
	countofx = index.count("x")
	countofo = index.count("o")
	countofdot = index.count(".")
	if sum(countofx + countofo + countofdot) != 9:
		return "invalid input"
	if abs(countofx - countofo) != 1:
		return "invalid game"



def main():
	'''main function for the tic-tac-toe game'''
	row = []
	for i in range(3):
		matrix = input()
		matrix = list(map(str, matrix.split()))
		row.append(matrix)
	# print(row)
	print(valid(row))



if __name__ == '__main__':
    main()

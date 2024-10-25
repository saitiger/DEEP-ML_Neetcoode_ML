def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
		rows = len(a) 
		columns = len(a[0])
		if columns!=len(b): # Checking if multiplication is possible i.e. Number of Columns of Matrix A and the Number of Columns of Matrix B are the same. 
			return -1
		res = []
		for i in range(rows):
			row_sum = 0
			for j in range(columns):
				row_sum+=a[i][j]*b[j]
			res.append(row_sum)
		return res

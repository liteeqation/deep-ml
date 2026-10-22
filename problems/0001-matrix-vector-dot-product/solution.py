def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if not a or not a[0]:
		return -1
	col_count=len(a[0])
	if col_count!=len(b):
		return -1
	result=[]
	for row in a:
		res_sum=sum(a*b for a,b in zip(row,b))
		result.append(res_sum)
	return result
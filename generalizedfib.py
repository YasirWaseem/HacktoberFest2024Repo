# Python3 program to implement the
# Generalised Fibonacci numbers

# Function to find the Nth term
def F(N, a, b, m, n):
	
	# m 1 
	# n 0 
	F = [[ m, 1 ], [ n, 0 ]]

	if(N == 0):
		return a
	if(N == 1):
		return b
	if(N == 2):
		return m * b + n * a

	initial = [[ m * b + n * b, b ],
						[ b, a ]]

	power(F, N - 2, m, n)

	multiply(initial, F)

	return F[0][0]

# Function that multiplies
# 2 matrices F and M of size 2*2,
# and puts the multiplication
# result back to F[][]
def multiply(F, M):
	
	x = (F[0][0] * M[0][0] +
		F[0][1] * M[1][0])

	y = (F[0][0] * M[0][1] +
		F[0][1] * M[1][1])

	z = (F[1][0] * M[0][0] +
		F[1][1] * M[1][0])

	w = (F[1][0] * M[0][1] +
		F[1][1] * M[1][1])

	F[0][0] = x
	F[0][1] = y
	F[1][0] = z
	F[1][1] = w

# Function that calculates F[][]
# raised to the power N
# and puts the result in F[][]
def power(F, N, m, n):

	M = [[ m, 1 ], [ n, 0 ]]
	for i in range(1, N + 1):
		multiply(F, M)

# Driver code
if __name__ == '__main__':

	N, a, b, m, n = 2, 0, 1, 2, 3
	print(F(N, a, b, m, n))

	N = 3
	print(F(N, a, b, m, n))

	N = 4
	print(F(N, a, b, m, n))

	N = 5
	print(F(N, a, b, m, n))

# This code is contributed by Shivam Singh

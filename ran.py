"""
input data:
2
A C M  X0 N
3 7 12 1 2
2 3 15 8 10
Xnext = (A * Xcur + C) % M
"""
Xcur = int(input("Enter a number:"))
A = 0
C = 0
M = 0

def random(Xcur):
	if Xcur ==0:
		for Xcur in range(1,10):
			A = 3
			C = 7
			M = 10
			Xnext = (A * Xcur + C) % M
			Xcur = Xnext
			N = 10
			Y = Xcur % N + 1
			#if N==2:
			print(Y)
	elif Xcur ==8:
		for N in range(1,15):
			A = 2
			C = 3
			M = 15
			Xnext = (A * Xcur + C) % M
			Xcur = Xnext
			#if N==10:
			print(Xnext)
random(Xcur)


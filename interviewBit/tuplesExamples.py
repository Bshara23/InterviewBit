
if __name__ == "__main__":
	arr = [1, 2 ,3 ,4, 5]
	
	softCopy = arr[:] #soft copy of the array, no pointers
	pointerCopy = arr #all changes made to pointerCopy is also applied to arr

	X = arr[1:]
	Y = arr[:1]
	Z = arr[1:2]

	print(X)
	
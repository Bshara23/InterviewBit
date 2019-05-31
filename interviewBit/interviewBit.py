
def merge(Arr, start, mid, end) :

	# create a temp array
	temp = [0] * (end - start + 1)

	# crawlers for both intervals and for temp
	i, j, k = start, mid+1, 0

	# traverse both lists and in each iteration add smaller of both elements in temp 
	while(i <= mid and j <= end) :
		if(Arr[i] <= Arr[j]) :
			temp[k] = Arr[i]
			k += 1; i += 1
		else :
			temp[k] = Arr[j]
			k += 1; j += 1

	# add elements left in the first interval 
	while(i <= mid):
		temp[k] = Arr[i]
		k += 1; i += 1

	# add elements left in the second interval 
	while(j <= end):
		temp[k] = Arr[j]
		k += 1; j += 1

	# copy temp to original interval
	for i in range (start, end + 1):
		Arr[i] = temp[i - start]


# Arr is an array of integer type
# start and end are the starting and ending index of current interval of Arr

def mergeSort(Arr, start, end):

	if(start < end):
		mid = (start + end) / 2
		mergeSort(Arr, start, mid)
		mergeSort(Arr, mid+1, end)
		merge(Arr, start, mid, end)


if __name__ == "__main__":
	arr = 1, 2 ,3 ,5 ,6 ,2, 3, 4, 1, 2, 3, 4, 5
	#mergeSort(arr, 0, len(arr) - 1)
	print(*arr)
	print(len(arr))

	# create a temp array
	temp = [6] * (20)
	print(*temp)
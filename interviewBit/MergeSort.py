# Auxiliary Space: O(n)

# Algorithmic Paradigm: Divide and Conquer

# Sorting In Place: No in a typical implementation

# Stable: Yes


# Python program for implementation of MergeSort 
def mergeSort(arr): 

    if len(arr) > 1: 

		# devide into two halfs to R and L
        mid = len(arr) // 2 
        L = arr[:mid] 
        R = arr[mid:]
  

        mergeSort(L) # Sort the first half 
        mergeSort(R) # Sort the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # add the remaining elements
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1


#if __name__ == "__main__":
#	arr = [1, 2 ,3 ,5 ,6 ,2, 3, 4, 1, 2, 3, 4, 5]
#	#mergeSort(arr, 0, len(arr) - 1)

#	#print(*arr)
#	#print(len(arr))

#	# create a temp array
#	#temp = [6] * (20)
#	#print(*temp)
#	X = arr[:]
#	X[1] = 0

#	print(X)
#	print(arr)